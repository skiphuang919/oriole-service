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
#     )                 Oriole-CF               (
#    (                  Eric.Zhou                )
#    '-------------------------------------------'
#

from oriole_service.api import MsConfig

# Create configuration for every microservice, not all.
# Etcd is required, or raise an exception.
_cf = MsConfig()

# Supply r/w for configuration files.
write, read = _cf.write, _cf.read
