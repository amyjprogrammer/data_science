#Import Libraries

import pandas as pd
import streamlit as st 
import altair as alt 
from PIL import Image

#Page Title
image = Image.open('DNA.png')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

#Input Text Box

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area('Sequence input', sequence_input, height=225)
sequence = sequence.splitlines()
sequence = sequence[1:] #skips the line title
sequence = ''.join(sequence)

st.write("""
***
""")

#Prints the whole DNA sequence
st.header('INPUT (DNA Query)')
sequence

#The count
st.header('OUTPUT (DNA Nucleotide Count)')

#Dictionary with the breakdown
st.subheader('1. Print Dictionary')
def DNA_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),       
        ])
    return d

Count = DNA_count(sequence)
Count

#Display info using text instead
st.subheader('2. Print text')
st.write('There are ' + str(Count['A']) + ' adenine (A)')
st.write('There are ' + str(Count['T']) + ' thymine (T)')
st.write('There are ' + str(Count['G']) + ' guanine (G)')
st.write('There are ' + str(Count['C']) + ' cytosine (C)')

#Display as a table
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(Count, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index': 'nucleotide'})
st.write(df)

#Bar Chart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80) #controls the width of the bars in the chart
)
st.write(p)