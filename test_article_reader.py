from article_reader import read_article

url = "https://arcprize.org/results/deepseek-v4-flash-0731"

text = read_article(url)

print(text[:1000])