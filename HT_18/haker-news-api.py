import requestsimport htmlimport reimport csvfrom datetime import datetime# Pay attention on class Stories/method(create_list_id)# when specifying different parameters, we get different results# askstories takes about 9 minutes# newstories takes about 11 minutes# showstories takes about 4 minutes# jobstories takes about 1 minutesclass CheckTopic:    """    class defines a category and creates        an instance of the corresponding class    ...    Attributes    topic: str        user-selected category    Methods    main        defines a category and creates        an instance    """    def __init__(self, topic=None):        """        constructor        :param topic: str            user-selected category        """        self.topic = topic    def main(self):        """        The method defines a category and creates        an instance of the corresponding class        :return: instance of the corresponding class        raise: ValueError            if category name not available        """        if self.topic == 'askstories':            return AskStories(self.topic)        elif self.topic == 'showstories':            return ShowStories(self.topic)        elif self.topic == 'newstories':            print("Be patient. It take a couple minutes")            return NewStories(self.topic)        elif self.topic == 'jobstories':            return JobStories(self.topic)        elif self.topic == '':            print("Be patient. It take a couple minutes")            return NewStories('newstories')        else:            raise ValueError(f"Category {self.topic} don't exist! askstories,"                             f" showstories, newstories, "                             f"jobstories are available")class Stories:    """    class for processing data received as a    result of sending requests to the hacker-news api    Attributes    topic: str        user-selected category    Methods    create_list_id        makes a request to the hacker-news api        and generates a list of ids    kids_ids        processes the id from the kids field    time_convert        convert timestamp to utc    clean_up_text        clears text with uts-8 encoding from html        tags and characters of other encodings    save_data        method sends requests to the hacker-news api        and formed list of dictionary and sent for saving    """    def __init__(self, topic):        """        constructor        :param topic: str            user-selected category        """        self.topic = topic        self.id_list = self._create_list_id()    def _create_list_id(self):        """        Method makes a request to the hacker-news api.        from the response generates a list of ids        in accordance with the category selected by the user        :return: list of story IDs for the selected category        """        url = f"https://hacker-news.firebaseio.com/v0/{self.topic}.json"        response = requests.get(url)        print(f"\nGet {self.topic} info. It can take some time\n____________")        id_list = []        #  10 id's for default        # specified index  - use only 10 ids        # not specified index - use all available id's. Take a lot of time!        for i_d in response.json():  # specify the number of ids here            id_list.append(i_d)        return id_list    def _kids_ids(self, comment_ids):        """        the method processes the id from the kids field. It sends requests        to the hacker-news api for all ids from the list(comment_ids).        Generates the result(comment author : comment ) as a dictionary.        The result of each query is added to the list.        :param comment_ids: id's from the kids field        :return: list of dictionaries        """        comment_list = []        for i_d in comment_ids:            url = f"https://hacker-news.firebaseio.com/v0/item/{i_d}.json"            article_response = requests.get(url)            article = article_response.json()            if 'deleted' in article.keys() or 'text' not in article.keys():                continue            author_comment = {                article['by']: self._clean_up_text(article['text'])            }            comment_list.append(author_comment)        return comment_list    @staticmethod    def _time_convert(time):        """ Method convert timestamp to utc """        utc_time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d  %H:%M')        return utc_time    @staticmethod    def _clean_up_text(text):        """ Convert all named and numeric character references         in the string to the corresponding Unicode characters """        clean_text = re.sub('<[^<]+?>', '', text)        clean_text = html.unescape(clean_text)        return clean_text    def _save_data(self, i_d):        """        the method sends requests to the hacker-news api        for all ids from the list(create_list_id).  query results        are formed list of dictionary and sent for saving        :param i_d: str            id from list        :return: list with dictionary inside        """        url = f"https://hacker-news.firebaseio.com/v0/item/{i_d}.json"        response = requests.get(url)        content_to_write = {}        for key, val in response.json().items():            if key == 'kids':                comments = self._kids_ids(val)                content_to_write.update({'comment': comments})            elif key == 'time':                content_to_write.update({key: self._time_convert(val)})                continue            elif key == 'title' or key == 'text':                clean_text = self._clean_up_text(val)                content_to_write.update({key: clean_text})                continue            content_to_write.update({key: val})        return [content_to_write]class AskStories(Stories):    """    the class generates instances to obtain information on a    particular category. Inherited from class Stories    Attributes    .....    Methods    get_data        The method makes queries on the generated list of id        numbers    """    def get_data(self):        """        The method makes queries on the generated list of id        numbers(method create_list_id) and saves it in the        corresponding table column in the csv file        """        with open(f"{self.topic}_.csv", 'w+', encoding='utf-8', newline='') as file:            fieldnames = [                'id', 'by',                'score', 'descendants',                'kids', 'title',                'text', 'time', 'comment',                'type'            ]            self.writer = csv.DictWriter(file, fieldnames=fieldnames, restval='No content')   # list(result.keys())            self.writer.writeheader()            for result in self.id_list:                self.writer.writerows(self._save_data(result))            print('Done\n')class NewStories(Stories):    """    the class generates instances to obtain information on a    particular category. Inherited from class Stories    Attributes    .....    Methods    get_data        The method makes queries on the generated list of id        numbers    """    def get_data(self):        """        The method makes queries on the generated list of id        numbers(method create_list_id) and saves it in the        corresponding table column in the csv file        """        with open(f"{self.topic}_.csv", 'w+', encoding='utf-8', newline='') as file:            fieldnames = [                'id', 'by',                'score', 'descendants',                'title', 'text',  'time',                'type', 'url', 'kids', 'comment'            ]            self.writer = csv.DictWriter(file, fieldnames=fieldnames, restval='No content')   # list(result.keys())            self.writer.writeheader()            for result in self.id_list:                self.writer.writerows(self._save_data(result))            print('Done\n')class JobStories(Stories):    """    the class generates instances to obtain information on a    particular category. Inherited from class Stories    Attribute    ....    Methods    get_data        The method makes queries on the generated list of id        numbers    """    def get_data(self):        """        The method makes queries on the generated list of id        numbers(method create_list_id) and saves it in the        corresponding table column in the csv file        """        with open(f"{self.topic}_.csv", 'w+', encoding='utf-8', newline='') as file:            fieldnames = [                'id', 'by',                'score', 'title',                'text', 'time',                'type', 'url'            ]            self.writer = csv.DictWriter(file, fieldnames=fieldnames, restval='No content')  # list(result.keys())            self.writer.writeheader()            for result in self.id_list:                self.writer.writerows(self._save_data(result))            print('Done\n')class ShowStories(Stories):    """    the class generates instances to obtain information on a    particular category. Inherited from class Stories    Attribute    ....    Methods    get_data        The method makes queries on the generated list of id        numbers    """    def get_data(self):        """        The method makes queries on the generated list of id        numbers(method create_list_id) and saves it in the        corresponding table column in the csv file        """        with open(f"{self.topic}_.csv", 'w+', encoding='utf-8', newline='') as file:            fieldnames = [                'id', 'by',                'score', 'descendants',                'title', 'text',                'time', 'type',                'url', 'kids', 'comment'            ]            self.writer = csv.DictWriter(file, fieldnames=fieldnames, restval='No content')  # list(result.keys())            self.writer.writeheader()            for result in self.id_list:                self.writer.writerows(self._save_data(result))            print('Done\n')if __name__ == "__main__":    category = input('Enter news category\n(available category - askstories, '                     'showstories, newstories, jobstories):  ').strip(" ")    autostart_category = CheckTopic(category)    start = autostart_category.main()    start.get_data()    # askstories = CheckTopic('askstories')    # newstories = CheckTopic('newstories')    # showstories = CheckTopic('showstories')    # jobstories = CheckTopic('jobstories')    # first_obj = askstories.main()    # first_obj.get_data()    # second_obj = newstories.main()    # second_obj.get_data()    # third_obj = showstories.main()    # third_obj.get_data()    # fourth_obj = jobstories.main()    # fourth_obj.get_data()