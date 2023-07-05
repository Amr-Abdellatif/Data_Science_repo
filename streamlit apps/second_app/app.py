import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

st.header("Insert DNA Sequence")

sequence_input = ('please enter \n.AAATTTCCCtGctat\n..aaaGaa\naaaaGGGGaaGGGa')


sequence = st.text_area("sequence input",sequence_input,height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = " ".join(sequence)

st.write("""
***
""")

st.header("input DNA query")
sequence

st.header("output DNA nucleotide output")


#part 1 
#print dictionary
st.subheader("1. print dictionary")
def DNA_nuc_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('C',seq.count('C')),
        ('G',seq.count('G')),
        ('T',seq.count('T'))
    ])
    return d


x = DNA_nuc_count(sequence)
x
x_label = list(x)
x_value = list(x.values())



st.subheader('2. print text')
st.write('there are ' + str(x['A']) + 'adenine (A)')
st.write('there are ' + str(x['C']) + 'thymine (C)')
st.write('there are ' + str(x['G']) + 'guanine (G)')
st.write('there are ' + str(x['T']) + 'thymine (T)')


st.subheader('3. display dataframe')

df = pd.DataFrame.from_dict(x,orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

st.subheader('4. display bar chart usin altair')
p = alt.Chart(df).mark_bar().encode(
    x= 'nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)
st.write(p)

