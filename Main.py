import streamlit as st
import mysql.connector
import pandas as pd
import datetime
from streamlit_option_menu import option_menu
import webbrowser


st.set_page_config(page_title="Library Management System",
                   page_icon="https://leadership-gold.com/wp-content/uploads/2016/06/Books-horizontal.jpg")
page_bg_img = """<style> [data-testid="stAppViewContainer"]
{ background-image: url(
"https://png.pngtree.com/back_origin_pic/00/12/31/318ed5171fca0954f79cd0215e3cf762.jpg"); 
background-size: cover;} 

    [data-testid="stHeader"]
    {background-color: rgba(0,0,0,0);
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)
header = '''
<h1><center>LIBRARY MANAGEMENT SYSTEM</center></h1>
<style> h1{font-size:50px
text-align: center;
visibility: visible;
display:table;
background-color:hsla(0,100%,50%,0.3);
position:relative;
padding:5px;
</style>
<style>
div.block-container{padding-top:1rem;}
</style>
'''
st.markdown(header, unsafe_allow_html=True)

hide_streamlit_style = '''
<style> #MainMenu{visibility:visible;}
footer{visibility:hidden;}
footer:after{
content:"Made By Shweta Dubey, Copyright @2022. All rights reserved";
font-size: medium;
text-align: center;
visibility: visible;
display:block;
background-color:hsla(0,100%,50%,0.3);
position:relative;
padding:5px;
top:2px;
}
</style>

'''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#buff, col, buff2 = st.columns([1, 3, 1])
            #st.session_state['uid'] = col.text_input('Username')
            #buff, col, buff2 = st.columns([1, 3, 1])
            #pwd = col.text_input("Password", type='password')
            #buff, col, buff2 = st.columns([10, 3, 10])
            #btn= col.button('Submit')
with st.sidebar:
    choice = option_menu(
        menu_title=None,
        options=["HOME", "STUDENT LOGIN", "STUDENT SIGNUP", "LIBRARIAN LOGIN"],
        icons=["house", "box-arrow-in-right", "person-plus-fill", "door-open-fill"],
        menu_icon="cast",
        default_index=0,
    )
if choice == "HOME":
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/HOW-DO-YOU-DESIGN-A-LIBRARY-MANAGEMENT-SYSTEM-min.png",
            width=350)
    with col2:
        st.header("About")
        content = "It is a Web Application which manages the data of Books, Issue Books,Student, Librarian so that the features such as Viewing Books,Issue the Books, Add the Books, Login ,etc can be performed.It uses Database Management System (DBMS) such as MySQL also this is build on framework called Streamlit.This Application can be accessed over a LAN (Local Area Network)" \
                  "This Application is developed by Shweta as a part of Training Project"
        st.write(content)
    st.markdown("<center><h2>Books in Library</h2></center>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns(3)
    with col3:
        st.markdown(
            '''<img src ="https://covers.openlibrary.org/b/id/1447159-M.jpg" width ='180' height='230' margin =''/>''',
            unsafe_allow_html=True)
        st.markdown("")
    with col4:
        st.markdown(
            '''<img src ="https://covers.openlibrary.org/b/id/1972357-M.jpg" width ='180' height='230'/>''',
            unsafe_allow_html=True)
    with col5:
        st.markdown(
            '''<img src ="https://covers.openlibrary.org/b/id/5829309-M.jpg" width ='180' height='230'/>''',
            unsafe_allow_html=True)
    col6, col7, col8 = st.columns(3)
    with col6:
        st.markdown(
            '''<img src ="https://covers.openlibrary.org/b/olid/OL10070074M-M.jpg" width ='180' height='225'/>''',
            unsafe_allow_html=True)
    with col7:
        st.markdown(
            '''<img src ="https://covers.openlibrary.org/b/id/8300232-M.jpg" width ='180' height='225'/>''',
            unsafe_allow_html=True)
    with col8:
        st.markdown(
            '''<img src ="https://covers.openlibrary.org/b/id/8243335-M.jpg" width ='180' height='225'/>''',
            unsafe_allow_html=True)
elif choice == "STUDENT LOGIN":
    st.markdown("<center><h1>HELLO STUDENT</h1></center>", unsafe_allow_html=True)
    if 'login' not in st.session_state:
        st.session_state['login'] = False
        st.session_state['sid'] = "s"
    if st.session_state['login'] == False:
        st.session_state['sid'] = st.text_input("Enter Student ID")
        pwd = st.text_input("Enter Password", type='password')
        btn = st.button("Login")
        if btn:
            mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
            c = mydb.cursor()
            c.execute("select * from student")
            for row in c:
                if (row[0] == st.session_state['sid'] and row[1] == pwd):
                    st.session_state['login'] = True
                    st.experimental_rerun()
                    break
            if (st.session_state['login'] == False):
                st.warning("Incorrect ID or Password")
                st.info("Go to SIGNUP Menu and register first")
    if st.session_state['login']:
        st.success("Login Successful")
        choice2 = st.selectbox("Features", ("None", "View All Books", "Issue Books"))
        if choice2 == "View All Books":
            mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
            c = mydb.cursor()
            c.execute("select * from books")
            l = []
            for row in c:
                l.append(row)
            df = pd.DataFrame(data=l, columns=['Book ID', 'Book Name', 'Author Name'])
            st.dataframe(df)
            def onclick(books):
                doi1 = str(datetime.datetime.now())
                mydb2 = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
                c2 = mydb2.cursor()
                c2.execute("insert into bookdata values(%s,%s,%s)", (doi1, st.session_state['sid'], books))
                mydb2.commit()
            st.markdown("<center><h2>Select Books</h2></center><style> h2{display:table; background-color:hsla(0,100%,50%,0.3); padding:3px; </style>", unsafe_allow_html=True)

            col3, col4, col5 = st.columns(3)
            with col3:
                st.markdown(
                    '''<img src ="https://covers.openlibrary.org/b/id/1447159-M.jpg" width ='180' height='230'/>''',
                    unsafe_allow_html=True)
                st.success("Book-id = 8003")
                if st.button("Open Book"):
                    webbrowser.open_new_tab(url="https://archive.org/details/haroldlastofsaxo0000lytt/mode/1up?ref=ol&view=theater")
                    onclick(books="8003")

            with col4:
                st.markdown(
                    '''<img src ="https://covers.openlibrary.org/b/id/1972357-M.jpg" width ='180' height='230'/>''',
                    unsafe_allow_html=True)
                st.success("Book-id = 8004")
                if st.button("Open Book", key="1"):
                    webbrowser.open_new_tab(url="https://archive.org/details/cihm_32590/mode/1up?ref=ol&view=theater")
                    onclick(books="8004")

            with col5:
                st.markdown(
                    '''<img src ="https://covers.openlibrary.org/b/id/5829309-M.jpg" width ='180' height='230'/>''',
                    unsafe_allow_html=True)
                st.success("Book-id = 8025")
                if st.button("Open Book", key="2"):
                    webbrowser.open_new_tab(
                        url="https://archive.org/details/vandoverbrute00norrrich/mode/1up?ref=ol&view=theater")
                    onclick(books="8025")

            col6, col7, col8 = st.columns(3)
            with col6:
                st.markdown(
                    '''<img src ="https://covers.openlibrary.org/b/olid/OL10070074M-M.jpg" width ='180' height='230'/>''',
                    unsafe_allow_html=True)
                st.success("Book-id = 8066")
                if st.button("Open Book", key="3"):
                    webbrowser.open_new_tab(
                        url="https://archive.org/details/advancescomputer14unkn/mode/1up?ref=ol&view=theater")
                    onclick(books="8066")

            with col7:
                st.markdown(
                    '''<img src ="https://covers.openlibrary.org/b/id/8300232-M.jpg" width ='180' height='230'/>''',
                    unsafe_allow_html=True)
                st.success("Book-id = 8094")
                if st.button("Open Book", key="4"):
                    webbrowser.open_new_tab(
                        url="https://archive.org/details/in.ernet.dli.2015.209962/mode/1up?ref=ol&view=theater")
                    onclick(books="8094")

            with col8:
                st.markdown(
                    '''<img src ="https://covers.openlibrary.org/b/id/8243335-M.jpg" width ='180' height='230'/>''',
                    unsafe_allow_html=True)
                st.success("Book-id = 8159")
                if st.button("Open Book", key="5"):
                    webbrowser.open_new_tab(
                        url="https://archive.org/details/ausgoethesitalie00goetuoft/mode/1up?ref=ol&view=theater")
                    onclick(books="8159")

        elif choice2 == "Issue Books":
            doi = str(datetime.datetime.now())
            mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
            c = mydb.cursor()
            c.execute("select * from books")
            l = []
            for row in c:
                l.append(row)
            list_of_books = [i[0] for i in l]
            selected_book = st.selectbox("Books", list_of_books)
            def select_book(bookid):
                mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
                c = mydb.cursor()
                c.execute("insert into issue values(%s,%s,%s)", (doi, bookid, st.session_state['sid']))
                mydb.commit()
            if st.button("issue book"):
                select_book(selected_book)
                st.success("Book issued successfully")
        btn2 = st.button("Logout")
        if btn2:
            st.session_state['login'] = False
elif (choice == "STUDENT SIGNUP"):
    st.markdown("<center><h1>Please Register if you're not a member</h1></center>", unsafe_allow_html=True)
    st.subheader("Create New Account")
    new_user = st.text_input("USERNAME")
    new_pwd = st.text_input("PASSWORD", type='password')
    btn4 = st.button("SIGNUP")
    if btn4:
        mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
        c = mydb.cursor()
        c.execute("insert into student values(%s,%s)", (new_user, new_pwd))
        mydb.commit()
        st.success("You have successfully created an account")
        st.info("Go to Login Menu to login")

elif (choice == "LIBRARIAN LOGIN"):
    st.markdown("<center><h1>HELLO LIBRARIAN</h1></center>", unsafe_allow_html=True)
    if 'llogin' not in st.session_state:
        st.session_state['llogin'] = False
    if st.session_state['llogin'] == False:
        sid = st.text_input("Enter Librarian ID")
        pwd = st.text_input("Enter Librarian Password", type='password')
        btn = st.button("LOGIN")
        if btn:
            mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
            c = mydb.cursor()
            c.execute("select * from librarian")
            for row in c:
                if (row[0] == sid and row[1] == pwd):
                    st.session_state['llogin'] = True
                    st.experimental_rerun()
                    break
            if (st.session_state['llogin'] == False):
                st.warning("Incorrect ID or Password")
    if st.session_state['llogin']:
        st.success("Login Successful")
        choice2 = st.selectbox("Features", ("None", "View Issue Books", "Add new Books", "Delete student"))
        if choice2 == "View Issue Books":
            mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
            c = mydb.cursor()
            c.execute("select * from issue")
            l = []
            for row in c:
                l.append(row)
            df = pd.DataFrame(data=l, columns=['Date of Issue', 'Book ID', 'Student ID'])
            st.dataframe(df)
        elif choice2 == "Add new Books":
            bid = st.text_input("Enter Book ID")
            bname = st.text_input("Enter Book Name")
            aname = st.text_input("Enter Author Name")
            btn3 = st.button("Add new Book")
            if btn3:
                mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
                c = mydb.cursor()
                c.execute("insert into books values(%s,%s,%s)", (bid, bname, aname))
                mydb.commit()
                st.header("Book Added Successfully")
        elif choice2 == "Delete student":
            mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
            c = mydb.cursor()
            c.execute("select * from student")
            l = []
            for row in c:
                l.append(row)
            list_of_students = [i[0] for i in l]
            selected_task = st.selectbox("Students to delete", list_of_students)
            def delete_data(studentid):
                mydb = mysql.connector.connect(host="localhost", user="root", password="SDs146@@#$$", database="lms")
                c = mydb.cursor()
                c.execute('delete from student where studentid = "{}" '.format(studentid))
                mydb.commit()
            if st.button("Delete"):
                delete_data(selected_task)
                st.success("Student deleted Successfully")
        btn2 = st.button("LOGOUT")
        if btn2:
            st.session_state['llogin'] = False
