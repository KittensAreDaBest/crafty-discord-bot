import requests
from urllib.parse import urljoin

from crafty_client.static.routes import MCAPIRoutes, CraftyAPIRoutes
from crafty_client.static.exceptions import *

# allow room for commander :)
class CraftyWeb():
    
    def __init__(self, url, api_token, verify_ssl=False):
        """ The main class for communicating with the Crafty Web API"""
        self.url = url
        self.verify_ssl = verify_ssl
        self.token = api_token
    
    def _unpack_response(self, response_dict):
        return response_dict['status'], response_dict['data'], response_dict['errors'], response_dict['messages']
    
    def _check_errors(self, errors, messages):
        if errors['error'] == 'ACCESS_DENIED':
            raise AccessDenied(messages['info'])
        elif errors['error'] == 'SER_NOT_RUNNING':
            raise ServerNotRunning()
        elif errors['error'] == 'NO_COMMAND':
            raise MissingParameters("Your request is missing essential parameters or they are invalid")
        elif errors['error'] == 'SER_RUNNING':
            raise ServerAlreadyRunning()
        elif errors['error'] == 'NOT_ALLOWED':
            raise NotAllowed(messages['info'])
        elif errors['error'] == 'NOT_FOUND':
            raise ServerNotFound(messages['info'])
        else:
            pass
    
    def _make_get_request(self, api_route, extra_params={}, body={}):
        api_location = urljoin(self.url, api_route)
        
        params = {'token': self.token}
        params.update(extra_params)
        
        with requests.get(api_location, verify=self.verify_ssl, params=params, data=body) as route:
            print(route.text)
            data = route.json()
            return self._unpack_response(data)
            
    def _make_post_request(self, api_route, extra_params={}, body={}):
        api_location = urljoin(self.url, api_route)
        
        params = {'token': self.token}
        params.update(extra_params)
        
        with requests.post(api_location, verify=self.verify_ssl, params=params, data=body) as route:
            print(route.text)
            data = route.json()
            return self._unpack_response(data)
        
    def list_mc_servers(self, by_name=False, all_data=False):
        """Asks Crafty for a list of servers"""
        status, data, errors, messages = self._make_get_request(MCAPIRoutes.LIST)
            
        if status == 200:
            if by_name:
                y = 0
                returnData = dict()
                for items in data['servers']:
                    returnData[y] = items.get("id", 0)
                    y += 1
                    returnData[y] = items.get("name", 0)
                return returnData
            if all_data:
                y = 0
                returnData = dict()
                for items in data['servers']:
                    returnData[y] = items.get("id", 0)
                    y += 1
                    returnData[y] = items.get("name", 0)
                    y += 1
                    returnData[y] = items.get("running", 0)
                    y = y + 1
                    returnData[y] = items.get("auto_start", 0)
                return returnData
                del returnData
            else:
                return data['servers']
        elif status == 500:
            self._check_errors(errors, messages)
    
    def start_server(self, server_id):
        """Tells crafty to start the specified server, raises ServerNotFound if crafty cannot find the server"""
        status, data, errors, messages = self._make_post_request(MCAPIRoutes.START, extra_params={'id': server_id})
        
        if status == 200:
            return True
        elif status == 500:
            self._check_errors(errors, messages)
    
    def stop_server(self, server_id):
        """Tells crafty to stop the specified server, raises ServerNotFound if crafty cannot find the server"""
        status, data, errors, messages = self._make_post_request(MCAPIRoutes.STOP, extra_params={'id': server_id})
        
        if status == 200:
            return True
        elif status == 500:
            self._check_errors(errors, messages)
    
    def backup_server(self, server_id):
        """Tells crafty to backup the specified server, raises ServerNotFound if crafty cannot find the server"""
        status, data, errors, messages = self._make_post_request(MCAPIRoutes.FORCE_BACKUP, extra_params={'id': server_id})
        
        if status == 200:
            return True
        elif status == 500:
            self._check_errors(errors, messages)

    def restart_server(self, server_id):
        """Tells crafty to restart the specified server, raises ServerNotFound if crafty cannot find the server"""
        status, data, errors, messages = self._make_post_request(MCAPIRoutes.RESTART, extra_params={'id': server_id})
        
        if status == 200:
            return True
        elif status == 500:
            self._check_errors(errors, messages)
    
    def search_server_logs(self, server_id, query_str):
        """Tells crafty to find logs with a specific pattern, raises ServerNotFound if crafty cannot find the server. Returned as list of dict."""
        status, data, errors, messages = self._make_post_request(MCAPIRoutes.SEARCH_LOGS, extra_params={'id': server_id, 'query': query_str})
        
        if status == 200:
            return data
        elif status == 500:
            self._check_errors(errors, messages)
    
    def get_server_logs(self, server_id):
        """Grabs the whole server log, raises ServerNotFound if crafty cannot find the server. Returned as list of dict."""
        status, data, errors, messages = self._make_get_request(MCAPIRoutes.GET_LOGS, extra_params={'id': server_id})
        
        if status == 200:
            return data
        elif status == 500:
            self._check_errors(errors, messages)
    
    def run_command(self, server_id, cmd):
        """Runs a command on the specified server, raises ServerNotFound if crafty cannot find the server. Returned as list of dict."""
        status, data, errors, messages = self._make_post_request(MCAPIRoutes.SEND_CMD, extra_params={'id': server_id}, body={'command':cmd})
        
        if status == 200:
            return data
        elif status == 500:
            self._check_errors(errors, messages)
    
    def get_host_stats_pc(self):
        """Grabs host PC stats from crafty"""
        status, data, errors, messages = self._make_get_request(CraftyAPIRoutes.HOST_STATS)
        
        if status == 200:
            return data
        elif status == 500:
            self._check_errors(errors, messages)
    
    def get_host_stats_server(self):
        """Grabs (mc) server stats from crafty"""
        status, data, errors, messages = self._make_get_request(CraftyAPIRoutes.SERVER_STATS)
        
        if status == 200:
            return data
        elif status == 500:
            self._check_errors(errors, messages)

