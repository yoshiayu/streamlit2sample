import streamlit as st
import time

st.title('Streamlit 入門')

st.write('ブログレスバー表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iterration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムにボタン')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3')

#text = st.text_input('趣味は')
#condition = st.slider('調子は?', 0, 100, 50)

#'好きな趣味:', text, 'です'
#'コンディション:', condition, 'です'

# if st.checkbox('Show Image'):
#    img = Image.open('sample01.jpg')
#    st.image(img, caption='ayumu', use_column_width=True)
