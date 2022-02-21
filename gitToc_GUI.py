from tkinter import Frame, Button, StringVar, Label

from tkinter import filedialog, messagebox
from gitToc import detectHeadLines


headline_dic={'#':0,'##':1,'###':2,'####':3,'#####':4,'######':5}
suojin={0:-1,1:-1,2:-1,3:-1,4:-1,5:-1,6:-1}
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.label = Label(self, text='Add a toc into Markdown File!')
        # self.label.pack()

        self.btn_select_file = Button(self, text='选择文件(select file)', command=self._select_file)
        self.btn_select_file.pack()

        self.text = StringVar()
        self.text.set('未选择文件(None selected)')
        self.label=Label(self, textvariable=self.text)
        self.label.pack()

        self.btn_excute = Button(self, text='执行转换(transform)', command=self._excute_parse)
        self.btn_excute.pack()

    def _excute_parse(self):
        if self.text.get() == '未选择文件(None selected)':
            messagebox.showwarning('错误(error)','未选择markdown文件!(None markdown file selected)')
            return
        f = open(self.filename,'r',encoding='utf-8')
        insert_str=detectHeadLines(f)
        f.close()
        with open('{}_with_toc.md'.format(self.filename[:self.filename.find('.')]),'w',encoding='utf-8') as f:
            f.write(insert_str)
        
        messagebox.showinfo('通知(Info)','转换已完成!(transform done.)')
        self.text.set('未选择文件(None selected)')
            
    def _select_file(self):
        self.filename = filedialog.askopenfilename(title='选择一个markdown文件(select markdown file)', \
                                                   filetypes=[('markdown file','*.md')])
        self.text.set(self.filename)

app = Application()

app.master.title('为你的markdown添加目录')

app.mainloop()