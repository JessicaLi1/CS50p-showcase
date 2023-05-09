import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Define regular expression for YouTube URLs
    yt_link = r'(http[s]?://)?(www\.)?youtube\.com/embed/([\w-]+)'

    #Search for URL in src attribute
    match=re.search(fr'<iframe .*?src="({yt_link})".*?>', s)

    if match:
        # Extract video ID from match and format as youtube URL
        video_id = match.group(4)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()