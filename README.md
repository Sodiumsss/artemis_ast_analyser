# artemis_ast_analyser
  
操作ast文件，提取&amp;回封

main.py->用于从ast文件中提取文本输出至astE中


back.py->用于从astE文件中提取文本回封至ast文件中



backtoback.py->需要原日文ast和现有提取文本文件，其中将JP行替换成原日文ast中的文本


暂时只支持文本操作，可能回漏掉少量文本。
back.py需要有new文件夹存在，否则报错。
