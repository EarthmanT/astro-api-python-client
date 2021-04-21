import os

from .sdk import VRClient
from .space_and_time import SpaceAndTime


class AstrologyCalls(object):

    def __init__(self):
        self.client = VRClient(
            os.environ.get('ASTRO_API_ID'),
            os.environ.get('ASTRO_API_KEY'))
        self.space_and_time = SpaceAndTime()

    @property
    def birth_details(self):
        return self.do_basic_call('birth_details')

    @property
    def astro_details(self):
        return self.do_basic_call('astro_details')

    def do_basic_call(self, api, args):
        api.extend(self.space_and_time.to_list())
        resp = self.client.call(*api)
        return resp.json()
