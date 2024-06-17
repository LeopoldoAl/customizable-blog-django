# https://docs.python.org/3.9/library/datetime.html#datetime.date.day
from datetime import datetime  # , date


class Commentaries:
    """ Works with comments send from a webpage """

    def __init__(self, data, table, **kwargs):
        self.data = data
        self.table = table
        self.kwargs = kwargs

    def commentexists(self, *args):
        """ Return the content inside the field that has been sent it """
        msg = ''
        if self.data is not None:
            msg = ''
            for i in self.data:
                if self.data[args[0]].strip() != '':
                    msg = self.data[args[0]].strip()
                    break
        return msg

    def sendingdata(self):
        # We save the data has sent from a comment
        if int(self.data['value']) == 0:
            self.data['value'] = 5
        got = self.table(
            value=self.data['value'],
            comment=self.data['comment'],
            article_id=self.kwargs['slug'],
            user_id=self.kwargs['user'],
            created=self.kwargs['date']
        )
        got.save()
        # We figure out if the data has already been saved
        confirm = self.table.objects.filter(value=self.data['value']
                                            , comment=self.data['comment']
                                            , user_id=self.kwargs['user'])[0]
        if str(confirm.user_id) == str(self.kwargs['user']):
            print(f"The user {self.kwargs['user']} has inserted a commentary!")
        return int(self.data['value'])

    def sendingdatareply(self):
        # We save the data has sent from a comment

        got = self.table(
            comment_identity=self.data['id_comment'],
            reply=self.data['reply'],
            article_id=self.kwargs['slug'],
            rating_id=self.kwargs['user2'],
            user_id=self.kwargs['user'],
            created=self.kwargs['date'],
        )
        got.save()
        # We figure out if the data has already been saved
        confirm = self.table.objects.filter(reply=self.data['reply']
                                            , user_id=self.kwargs['user'])[0]
        if str(confirm.user_id) == str(self.kwargs['user']):
            print(f"The user {self.kwargs['user']} has inserted a reply!")
        return int(1)

    def time_comment_recent(self):
        """ We get the date when the comment has done. """

        # We figure out if the data has already been saved
        date = self.table.objects.filter(value=self.data['value']
                                         , comment=self.data['comment']
                                         , user_id=self.kwargs['user'])[0]
        return date.created

    def working_date_time(self, time_date, exactitude=None):

        """ It works with date and time """

        difference_in_seconds = 0
        if datetime.today().astimezone().date() != time_date.astimezone().date():
            difference_in_seconds = (datetime.today().astimezone()
                                     - time_date.astimezone()).total_seconds()
        seconds = difference_in_seconds + (datetime.today().astimezone().hour * 60 * 60
                                           + datetime.today().astimezone().minute * 60
                                           + datetime.today().astimezone().second
                                           - (time_date.astimezone().hour * 60 * 60
                                              + time_date.astimezone().minute * 60
                                              + time_date.astimezone().second))
        if seconds < 60:
            answer = f"Written, {seconds} second ago" if seconds <= 1 else f"Written, {seconds} seconds ago"
        elif 60 <= seconds < 3600:
            answer = f"Written, {round(seconds / 60, exactitude)} minute ago" if round(
                seconds / 60) == 1 else f"Written, {round(seconds / 60, exactitude)} minutes ago"
        elif 3600 <= seconds < 86400:
            answer = f"Written, {round(seconds / 3600, exactitude)} hour ago" if round(
                seconds / 3600) == 1 else f"Written, {round(seconds / 3600, exactitude)} hours ago"
        elif 86400 <= seconds < 31536000:
            answer = f"Written, {round(seconds / 86400, exactitude)} day ago" if round(
                seconds / 86400) == 1 else f"Written, {round(seconds / 86400, exactitude)} days ago"
        elif 31536000 <= seconds < 3153600000:
            answer = f"Written, {round(seconds / 31536000, exactitude)} year ago" if round(
                seconds / 31536000) == 1 else f"Written, {round(seconds / 31536000), exactitude} years ago"
        elif 3153600000 <= seconds < 31536000000:
            answer = f"Written, {round(seconds / 3153600000, exactitude)} century ago" if round(
                seconds / 3153600000) == 1 else f"Written, {round(seconds / 3153600000, exactitude)} centuries ago"
        else:
            answer = f"Written, {round(seconds / 31536000000, exactitude)} millennium ago" if round(
                seconds / 31536000000) == 1 else f"Written, {round(seconds / 31536000000, exactitude)} millenniums ago"
        return answer
