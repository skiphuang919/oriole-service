#
#                __   _,--="=--,_   __
#               /  \."    .-.    "./  \
#              /  ,/  _   : :   _  \/` \
#              \  `| /o\  :_:  /o\ |\__/
#               `-'| :="~` _ `~"=: |
#                  \`     (_)     `/
#           .-"-.   \      |      /   .-"-.
#    .-----{     }--|  /,.-'-.,\  |--{     }-----.
#     )    (_)_)_)  \_/`~-===-~`\_/  (_(_(_)    (
#    (                                           )
#     )                 Oriole-DB               (
#    (                  Eric.Zhou                )
#    '-------------------------------------------'
#

from weakref import WeakKeyDictionary

from nameko.extensions import DependencyProvider

from oriole.db import *

Base = declarative_base()


class Db(DependencyProvider):
    def __init__(self, Base, uri="database"):
        self.base = Base
        self.uri = uri
        self.dbs = WeakKeyDictionary()

    def setup(self):
        self.bind = get_engine(self.container.config.get(self.uri))
        self.base.metadata.create_all(self.bind)

    def stop(self):
        self.bind.dispose()
        del self.bind

    def get_dependency(self, worker_ctx):
        session = get_session(self.bind)
        self.dbs[worker_ctx] = session

        return session

    def worker_teardown(self, worker_ctx):
        session = self.dbs.pop(worker_ctx)
        session.close()


class Rs(DependencyProvider):
    def setup(self):
        self.rs = get_redis(self.container.config.get("datasets"))

    def get_dependency(self, worker_ctx):
        return self.rs
