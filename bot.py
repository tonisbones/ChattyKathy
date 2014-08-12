from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc 

class ChattyKathyBot(irc.IRCClientt):
    def connectionMade(self):
        self.nickname = self.factory.nickname
        self.realname = self.factory.realname
        irc.IRCClient.connectionMade(self)
        log.msg("connectionMade")

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        log.msg("connectionLost {!r}".format(reason))

    def signedOn(self):
        log.msg("Signed on")
        if (self.nickname != self.factory.nickname:
            log.msg('Your nickname was already occupied, actual nickname is ''"{}.'.format(self,nickname))
        self.join(self.factory.channel)

    def joined(self, channel):
        log.msg("[{nick} has joined {channel}]".format(nick=self.nickname, channel=self.factory.channel,))

    def privmsg(self, user, channel, msg):

class ChattKathyBotFactory(protocol.ClientFactory):
    protocol = ChattyKathyBot
    def __init__(self, settings):
        self.channel = channel
        self.nickname = nickname
        self.realname = realname


