from blog import Blog


blogs = dict()
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "p" to create post, or "q" to quit.'


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    title = input('Enter the title of a new blog: ')
    author = input('Enter the name of the author of blog: ')
    created_blog = Blog(title, author)
    blogs[title] = created_blog

def ask_read_blog():
    title = input('Enter the title of the post whether you want to read: ')


def ask_create_post():
    title = input('Enter the title of the new post: ')
    content = input(f'Enter the content of post {title}: ')

