music = [{'name': 'Rivers and Roads', 'length': '4:44'},
         {'name': 'Requiem', 'length': '4:20'},
         {'name': 'Birthday Party', 'length': '3:44'},
         {'name': 'High Places (Acoustic)', 'length': '3:20'},
         {'name': 'For the Dancing and the Dreaming', 'length': '2:55'},
         {'name': 'Close your Eyes', 'length': '3:19'},
         {'name': 'Bumper Cars', 'length': '4:00'},
         {'name': 'Tied Together with a Smile', 'length': '4:08'},
         {'name': 'Sailboat Bed', 'length': '4:01'},
         {'name': 'I Want Us', 'length': '4:07'},
         {'name': '1995', 'length': '3:04'},
         {'name': 'I Hate This', 'length': '3:09'},
         {'name': 'Flames', 'length': '3:56'},
         {'name': 'Tetris', 'length': '2:50'},
         {'name': 'Keeping Score - Acoustic', 'length': '3:32'},
         {'name': 'Into You', 'length': '3:12'},
         {'name': 'Never Enough', 'length': '3:28'},
         {'name': 'Running', 'length': '3:57'},
         {'name': 'Theres No Way', 'length': '2:55'},
         {'name': 'No New Friends', 'length': '2:56'},
         {'name': 'Hold My Hand', 'length': '3:48'},
         {'name': 'Swim', 'length': '2:24'},
         {'name': 'Attention', 'length': '3:29'},
         {'name': 'Outrunning Karma', 'length': '3:09'},
         {'name': 'Apple', 'length': '2:44'},
         {'name': '100 Bad Days', 'length': '3:33'},
         {'name': 'Dynamite', 'length': '3:52'},
         {'name': 'Glory and Gore', 'length': '3:31'},
         {'name': 'I think Were alone now', 'length': '3:49'},
         {'name': 'Drunk in the Morning', 'length': '3:23'},
         {'name': 'Elastic Heart', 'length': '4:17'}]

music2 = [{'name': 'Rivers and Roads', 'length': '4:44'},
          {'name': 'Requiem', 'length': '4:20'},
          {'name': 'Birthday Party', 'length': '3:44'},
          {'name': 'High Places (Acoustic)', 'length': '3:20'},
          {'name': 'For the Dancing and the Dreaming', 'length': '2:55'},
          {'name': 'Close your Eyes', 'length': '3:19'},
          {'name': 'Bumper Cars', 'length': '4:00'},
          {'name': 'Tied Together with a Smile', 'length': '4:08'}]


def get_attribute_from_dict_list(dict_list, attribute):
    return [item[attribute] for item in dict_list]


def parse_time(time):
    minutes = int(time[:time.index(':')])
    seconds = int(time[time.index(':') + 1:])
    return (minutes * 60) + seconds


class NumberConsumer:
    def __init__(self, target, variance=0):
        self.int_list = []
        self.possible_sums = []
        self.target_list = []
        self.found_sum = -1
        self.min_target = target - variance
        self.max_target = target + variance

    def consume_int(self, num):
        self.possible_sums.append(num)
        self.int_list.append(num)
        if (num >= self.min_target) and (num <= self.max_target):
            self.found_sum = len(self.possible_sums)
        # Create a copy of the current array of sums - the most recent addition(we don't want to add a number to itself)
        possible_sum_copy = [element for element in self.possible_sums[:len(self.possible_sums)-1]]
        for possible_sum in possible_sum_copy:
            self.possible_sums.append(possible_sum + num)
            if (possible_sum + num >= self.min_target) and (possible_sum + num <= self.max_target):
                self.found_sum = len(self.possible_sums)

    @staticmethod
    def decimal_to_reverse_binary(num):
        # Returns the reverse binary of an integer
        # eg. 4 = 001, 20 = 00101
        binary = bin(num)[2:]
        reverse = str(binary)[::-1]
        return reverse

    def get_target_list(self):
        """:rtype: list"""
        if self.target_list:
            return self.target_list
        if self.found_sum == -1:
            return []
        # We have found the target sum in the possible sum list, and have set found_sum to the position of the sum
        # in possible sum list
        # found sum will correlate directly and in a very bizarre way to the solution to this problem
        # Lets trace a given found sum to take a peek into that correlation
        # Let's assume the 46th addition to possible sum was within the target range, and so found sum would be 46,
        binary_num = self.decimal_to_reverse_binary(self.found_sum)
        # We have converted 46 to binary and flipped it
        # 46 = 101110 = 011101 --Important note! Because each time we consume a number we basically double the length of
        # possible sums, this binary number is guaranteed to be equal in length to target list
        # Now we simply go through the original list of integers and accept it if the corresponding bit is a 1
        for i in range(len(binary_num)):
            if binary_num[i] == '1':
                self.target_list.append(self.int_list[i])
        return self.target_list


def create_playlist(songs, length_in_seconds, variance=0):
    songs = [song for song in songs]
    playlist = []
    song_lengths = get_attribute_from_dict_list(songs, 'length')
    parsed_song_lengths = list(map(parse_time, song_lengths))
    numbers_consumer = NumberConsumer(length_in_seconds, variance)
    i = 0
    # Use the consumer to get the correct list of ints
    while not numbers_consumer.get_target_list() and i < len(parsed_song_lengths):
        numbers_consumer.consume_int(parsed_song_lengths[i])
        i += 1
    target_times = numbers_consumer.get_target_list()
    # We have the times, now we need the song names
    for time in target_times:
        for song in songs:
            if parse_time(song['length']) == time:
                playlist.append(song['name'])
                songs.pop(songs.index(song))
                break
    return playlist


def test():
    print(create_playlist(music2, 544, 0))  # ['Rivers and roads', 'Birthday Party']
    print(create_playlist(music2, 488, 0))  # ['Tied Together With a Smile', 'Bumper Cars']
    print(create_playlist(music2, 50, 0))  # Some appropriate error
    print(create_playlist(music2, 488, 10))  # ['Requiem', 'Birthday Party']
    print(create_playlist(music, 3600, 0))  # ['Requiem', 'Birthday Party', 'High Places (Acoustic)',
    #  'For the Dancing and the Dreaming', 'Close your Eyes', 'Bumper Cars', 'Tied Together with a Smile',
    # 'Sailboat Bed', 'I Want Us', '1995', 'I Hate This', 'Flames', 'Tetris', 'Keeping Score - Acoustic', 'Into You',
    # 'Never Enough', 'Theres No Way']


def main():
    test()


main()
