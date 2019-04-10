pd.set_option('max_colwidth', 200)
pd.options.display.max_rows = 999


toy.alltext=toy.alltext.apply(lambda x: re.sub("(\d+\%)+([a-z]+)|([a-z]+)+(\d+\%)", "\\2  \\2\\1  \\3  \\3\\4",x))
