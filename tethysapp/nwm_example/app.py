from tethys_sdk.base import TethysAppBase, url_map_maker


class NwmExample(TethysAppBase):
    """
    Tethys app class for Nwm Example.
    """

    name = 'Nwm Example'
    index = 'nwm_example:home'
    icon = 'nwm_example/images/icon.gif'
    package = 'nwm_example'
    root_url = 'nwm-example'
    color = '#8e44ad'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='nwm-example',
                controller='nwm_example.controllers.home'
            ),
            UrlMap(
                name='medium_range',
                url='nwm-example/range/medium',
                controller='nwm_example.controllers.medium_range'
            ),
        )

        return url_maps
