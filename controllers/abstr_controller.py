from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from utility.constants import user_agents, REA_ROOT_LOGGER
import abc
import logging

logger = logging.getLogger(REA_ROOT_LOGGER + '.CTRL')


class CrawlRunner(object):

    def __init__(self, delay=1, req_per_ip=0, agent=0):
        self.logger = logger
        settings = get_project_settings()
        settings.set('LOG_LEVEL', 'WARN')
        settings.set('DOWNLOAD_DELAY', delay)
        settings.set('CONCURRENT_REQUESTS_PER_IP', req_per_ip)
        settings.set('AUTOTHROTTLE_TARGET_CONCURRENCY', 0.5)
        settings.set('COOKIES_ENABLED', False)
        settings.set('USER_AGENT', user_agents[agent])
        self. process = CrawlerProcess(settings)

    @abc.abstractmethod
    def run(self):
        return


class BatchDispatcher(object):
    def __init__(self):
        self.logger = logger
        return

    @abc.abstractmethod
    def dispatch_jobs(self):
        return
