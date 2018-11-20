#You can post on any blogger somehow

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import sys
import webscrape
from oauth2client import client
from googleapiclient import sample_tools


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'blogger', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/blogger')

  try:

      users = service.users()

      # Retrieve this user's profile information
      thisuser = users.get(userId='self').execute()
      print('This user\'s display name is: %s' % thisuser['displayName'])

      blogs = service.blogs()

      # Retrieve the list of Blogs this user has write privileges on
      thisusersblogs = blogs.listByUser(userId='self').execute()
      for blog in thisusersblogs['items']:
        print('The blog named \'%s\' is at: %s' % (blog['name'], blog['url']))

      posts = service.posts()
      body = {
        "kind": "blogger#post",
        "id": "3466134283062417425",
        "title": webscrape.news(),
        "content":"<div><b>It's Working Fine.. Seriously..</b></div>"
        }
      insert = posts.insert(blogId='3466134283062417425', body=body)
      posts_doc = insert.execute()
      print posts_doc


  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run'
      'the application to re-authorize')
if __name__ == '__main__':
  main(sys.argv)

