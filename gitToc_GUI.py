from tkinter import *

from tkinter import filedialog, messagebox



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
            messagebox.showwarning('错误(error)','未选择markdown文件！(None markdown file selected)')
            return
        f = open(self.filename,'r',encoding='utf-8')
        insert_str=self.detectHeadLines(f)
        f.close()
        with open('{}_with_toc.md'.format(self.filename[:self.filename.find('.')]),'w',encoding='utf-8') as f:
            f.write(insert_str)
        
        messagebox.showinfo('通知(Info)','转换已完成！(transform done.)')
        self.text.set('未选择文件(None selected)')
            
    def _select_file(self):
        self.filename = filedialog.askopenfilename(title='选择一个markdown文件(select markdown file)', \
                                                   filetypes=[('markdown file','*.md')])
        self.text.set(self.filename)


    def detectHeadLines(self, f):
        '''detact headline and return inserted string.

        params:
            f: Markdown file
        '''
        f.seek(0)

        insert_str=""
        org_str=""

        last_status = -1
        c_status=-1

        headline_counter=0
        iscode=False
        for line in f.readlines():
            if(line[:3]=='```'):
                iscode= not iscode
                
            # fix code indent bug.
            if not iscode:
                line=line.strip(' ')
            ls=line.split(' ')

            if len(ls)>1 and ls[0] in headline_dic.keys() and not iscode:
                headline_counter+=1
                c_status=headline_dic[ls[0]]
                # find first rank headline
                if last_status==-1 or c_status==0 or suojin[c_status]==0:
                    # init suojin
                    for key in suojin.keys():
                        suojin[key]=-1
                    suojin[c_status]=0
                elif c_status>last_status:
                    suojin[c_status]=suojin[last_status]+1
                
                # update headline text
                headtext=' '.join(ls[1:-1])
                if ls[-1][-1]=='\n':
                    headtext+=(' '+ls[-1][:-1])
                else:
                    headtext+=(' '+ls[-1])
                headid = '{}{}'.format('head',headline_counter)
                headline=ls[0]+' <span id=\"{}\"'.format(headid)+'>'+ headtext+'</span>'+'\n'
                org_str+=headline

                jump_str='- [{}](#{}{})'.format(headtext,'head',headline_counter)
                insert_str+=('\t'*suojin[c_status]+jump_str+'\n')
                        
                last_status=c_status
            else:
                org_str+=line
                
                
        return insert_str+org_str

app = Application()

app.master.title('为你的markdown添加目录')

app.mainloop()