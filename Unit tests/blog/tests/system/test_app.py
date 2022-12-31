from unittest import TestCase
from unittest.mock import patch
import app
from post import Post
from blog import Blog


class AppTest(TestCase):

    def setUp(self):
        blog = Blog('Test', "Test Author")
        app.blogs = {'Test': blog}


    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                with patch('app.print_posts') as mocked_print_post:

                    mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                    mocked_print_post(app.blogs['Test'])
                    app.menu()

                    mocked_ask_create_blog.assert_called()


    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:

                mocked_input.side_effect = ('p', 'Test', 'Test Title', 'Test Content', 'q')
                app.ask_create_post()
                app.menu()

                mocked_ask_create_post.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:

                mocked_input.side_effect = ('l', 'q')

                app.menu()

                mocked_print_blogs.assert_called()


    def test_menu_calls_ask_read_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:

                mocked_input.side_effect = ('r ', 'Test', 'q')

                app.menu()

                mocked_ask_read_blog.assert_called()


    def test_menu_print_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blod(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        app.blogs['Test'].create_post('Test Post', 'Test Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['Test'])

            mocked_print_post.assert_called_with(app.blogs['Test'].posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Test Content')
        expected_result = '''

--- Post Title ---

Test Content

'''

        with patch('builtins.print') as mocked_print_post:
            app.print_post(post)
            mocked_print_post.assert_called_with(expected_result)


    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')
            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')
