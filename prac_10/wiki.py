import wikipedia

def get_wikipedia_page(title):
    try:
        page = wikipedia.page(title, autosuggest=False)
        return page
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        for option in e.options[:5]:  # Show only the first 5 options for brevity
            print(option)
    except wikipedia.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    except Exception as e:
        print(f"An error occurred: {e}")

def print_page_details(page):
    print(f"\n{page.title}\n{page.summary[:500]}...\n{page.url}\n")

def main():
    while True:
        title = input("Enter a Wikipedia page title or search phrase (or press Enter to quit): ")
        if title.strip() == "":
            print("Thank you.")
            break
        page = get_wikipedia_page(title)
        if page:
            print_page_details(page)

if __name__ == "__main__":
    main()