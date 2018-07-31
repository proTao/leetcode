from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_table = defaultdict(set)
        self.twitters = defaultdict(list)
        self.timestamp = 65535
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.twitters[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.follow_table[userId]:
            self.follow_table[userId].add(userId)

        seeds = heapq.merge(*(self.twitters[i][::-1] for i in self.follow_table[userId]))
        res = []
        i = 0
        try:
            next_twitter = next(seeds)
            while i < 10:
                res.append(next_twitter[1])
                next_twitter = next(seeds)
                i += 1
        except StopIteration:
            pass
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId and followeeId not in self.follow_table[followerId]:
            self.follow_table[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId and followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,"5")
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.postTweet(2,"6")

print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))
