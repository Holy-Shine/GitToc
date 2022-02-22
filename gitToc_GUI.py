from tkinter import Tk, Frame, Button, StringVar, Label, Menu

from tkinter import filedialog, messagebox, IntVar
from gitToc import detectHeadLines

headline_dic={'#':0,'##':1,'###':2,'####':3,'#####':4,'######':5}
suojin={0:-1,1:-1,2:-1,3:-1,4:-1,5:-1,6:-1}


class Language():
    '语言包'
    EN = {
        'title': 'markdown TOC Generator',
        'language': '语言',
        'btn_select_file': 'select file',
        'status_text': 'None selected',
        'btn_excute': 'transform',
        'error': 'error',
        'info': 'info',
        'no_markdown_select': 'None of markdown file selected!',
        'transform_done': 'transform done.',
        'filename_dlg_title': 'select markdown file',
        'about':'about'
    }

    CN = {
        'title': 'markdown目录生成器',
        'language': 'language',
        'btn_select_file': '选择文件',
        'status_text': '未选择文件',
        'btn_excute': '执行转换',
        'error': '错误',
        'info': '提示',
        'no_markdown_select': '未选择markdown文件!',
        'transform_done': '转换完成.',
        'filename_dlg_title': '选择一个markdown文件',
        'about':'关于'
    }


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.ln_choice=IntVar()
        self.ln_choice.set(1) #OFFICEOpen默认选中
        self.language_pkg = Language.CN
        
        self.pack()
        self.createWidgets()

    def refresh_language(self):
        '刷新语言'

        # 简中
        if self.ln_choice.get()==1:
            self.language_pkg = Language.CN
        elif self.ln_choice.get()==2:
            self.language_pkg = Language.EN

        # 修改标题
        self.master.title(self.language_pkg['title'])
        # 修改按钮文字
        self.btn_excute.config(text=self.language_pkg['btn_excute'])
        self.btn_select_file.config(text=self.language_pkg['btn_select_file'])
        # 修改提示文字
        self.status_text.set(self.language_pkg['status_text'])
        # 修改菜单
        self.menu_bar.entryconfigure(1, label=self.language_pkg['language'])
        self.menu_bar.entryconfigure(2, label=self.language_pkg['about'])

    def createWidgets(self):
        # self.label = Label(self, text='Add a toc into Markdown File!')
        # self.label.pack()

        self.master.title('markdown目录生成器')

        # 菜单栏
        self.menu_bar = Menu(self)
    
        # 语言栏
        self.language_menu=Menu(self.menu_bar,tearoff=False)
        self.menu_bar.add_cascade(label='language',menu=self.language_menu)
        self.language_menu.add_radiobutton(label='简体中文',variable=self.ln_choice,value=1,command=self.refresh_language)
        self.language_menu.add_radiobutton(label='English',variable=self.ln_choice,value=2, command=self.refresh_language)

        # 关于栏
        self.about_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label='关于', menu=self.about_menu)
        self.about_menu.add_checkbutton(label='Author:Holy-Shine@GitHub')
        self.about_menu.add_separator()

        self.master.config(menu=self.menu_bar)

        self.btn_select_file = Button(self, text='选择文件', command=self._select_file)
        self.btn_select_file.pack()

        self.status_text = StringVar()
        self.status_text.set('未选择文件')
        self.label=Label(self, textvariable=self.status_text)
        self.label.pack()

        self.btn_excute = Button(self, text='执行转换', command=self._excute_parse)
        self.btn_excute.pack()

    def _excute_parse(self):
        if self.status_text.get() == self.language_pkg['status_text'] or self.status_text.get()=='':
            messagebox.showwarning(self.language_pkg['error'],self.language_pkg['no_markdown_select'])
            return
        f = open(self.filename,'r',encoding='utf-8')
        insert_str=detectHeadLines(f)
        f.close()
        with open('{}_with_toc.md'.format(self.filename[:self.filename.find('.')]),'w',encoding='utf-8') as f:
            f.write(insert_str)
        
        messagebox.showinfo(self.language_pkg['info'],self.language_pkg['transform_done'])
        self.status_text.set(self.language_pkg['status_text'])
            
    def _select_file(self):
        self.filename = filedialog.askopenfilename(title=self.language_pkg['filename_dlg_title'], \
                                                   filetypes=[('markdown file','*.md')])
        self.status_text.set(self.filename)


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x100')

    app = Application(master=root)
    app.mainloop()