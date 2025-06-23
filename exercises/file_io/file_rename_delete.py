import os
os.remove("novel.txt")  # delete file

os.rename("first_draft.txt", "term_paper.txt") #rename file

os.path.exists("userlist.txt")  #checks to see if file exists (if exists True, if not False)
