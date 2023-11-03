import streamlit as st
from helper_components import ColoredHeader, Notif

ColoredHeader(
    "Tech Trek | Fine Tuning Gpt’s",
    description=""
)

st.title("Introduction")
st.write('''You must have used the Chat With Document or Chat with Data
option in Chat-gpt. Discover how the dynamic combination of
GPT-3 and Llama-Index can create a new version of gpt models.
By the end of the workshop You’ll be able to create a new gpt
model whose responses would be specific to your dataset.
''')

st.title("Pre-requisites")
# modules required are openai streamlit, llama-index
st.write("1. OpenAI")
st.code("pip install openai")
st.write("2. Llama-index")
st.code("pip install llama-index")
st.write("3. Streamlit")
st.code("pip install streamlit")
st.write("4. OpenAI API key")
st.write("Check out this [Link](https://platform.openai.com/account/api-keys)")

ColoredHeader(
    "Lets Start Coding",
    description=" Lets start with the basic api usage"
)

st.code('''
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Generate text
prompt = "Write a poem about a cat."
response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=100
)

# Print the response
print(response.choices[0].text)

''')

st.title("Explanation")
st.divider()
st.subheader("1. Importing the openai module")
st.code(r"import openai")
st.markdown("*Needed to use the OpenAI API*")

st.subheader("2. Setting the OpenAI API key")
st.code("openai.api_key = \"YOUR_API_KEY\"")
st.markdown("*Replace YOUR_API_KEY with your API key*")

st.subheader("3. Choosing Prompt")
st.code('''prompt = "Write a poem about a cat."''')
st.markdown("*This is the prompt that will be used to generate the response*")

st.subheader("4. Generating the response")
st.code(r'''
response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=100
)
''')
st.markdown("*The response is stored in the response variable, This is basically the response you would get on the ChatGPT website if you would type the same prompt in the chatbox*")

ColoredHeader(
    "Lets Try Customizing It!",
    description="We will be using the llama-index module for this"
)

st.code('''
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

print("Setting up API Key...")
# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def load_data():
    reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
    docs = reader.load_data()
    service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert in analyzing student data of their particular University, Assume all input prompts to be with respect to the input data, Don't answer anything apart from educational related prompt"))
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    return index

index = load_data()

# Initialize the chat engine
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
while True:
    prompt = input("Your question: ")
    if not prompt:
        break
    # Generate a response
    response = chat_engine.chat(prompt)
    print("Assistant:", response.response)
''')

st.title("Explanation")
st.divider()

st.subheader("1. Importing the Required Modules")

st.code("from llama_index import VectorStoreIndex, ServiceContext")
st.markdown("*Needed to use the llama-index module*")
st.markdown('''* `VectorStoreIndex`, in simple terms, is a tool that makes your text data understandable to a computer by converting it into numbers, and it does this with the help of a specialized language model (LLM). This can be useful for various applications like text analysis, searching, and machine learning.''')
st.markdown('''* `ServiceContext`, in simple terms, is like the control center for managing your text-related tasks. It's the part of the `llama_index` module that helps you set things up and keep track of what's going on.''')
st.code("from llama_index.llms import OpenAI")
st.markdown('''* `OpenAI`, in simple terms, is like a bridge to a very smart computer program. This computer program, called an OpenAI language model, is excellent at understanding and working with text.''')
st.code("from llama_index import SimpleDirectoryReader")
st.markdown('''* `SimpleDirectoryReader`, in simple terms, is a tool that helps you load text data from a directory on your computer.''')

st.subheader("2. Setting the OpenAI API key")
st.code("openai.api_key = \"YOUR_API_KEY\"")
st.markdown("*Replace YOUR_API_KEY with your API key*")

st.subheader("3. Loading the Data")
st.code(r'''
def load_data():
    reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
    docs = reader.load_data()
    service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert in analyzing student data of their particular University, Assume all input prompts to be with respect to the input data, Don't answer anything apart from educational related prompt"))
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    return index
    ''')
st.markdown("*This function loads the data from the data folder and returns the index*")


# MAY NEED TO BE SIMPLIFIED
st.divider()
st.markdown('''
 
This is the function `load_data()` where we are feeding our dataset folder into
llama_index and openai model, and generating vectors out of it.

1. `reader = SimpleDirectoryReader(input_dir="./data", recursive=True)`: 

This line creates an instance of the `SimpleDirectoryReader` class from Llama-Index. It specifies the
input directory as "./data" (Basically the folder where you custom datasets will be stored) and sets the `recursive` parameter to `True`, indicating that
it should recursively search for files in subdirectories as well.

2. `docs = reader.load_data()`: 

The `load_data()` function is called on the `reader`
object, which reads the data from the specified directory and returns a list of
`Document` objects. Each `Document` represents a file in the directory.

3. `service_context = ServiceContext.from_defaults()`:

This line creates a `ServiceContext` object using the `from_defaults()` method. It configures the context
with an OpenAI language model (`llm`) using the GPT-3.5 Turbo model. The `temperature`
parameter sets the randomness of the model's responses, and the `system_prompt`
provides a system-level prompt for the model.

4. `index = VectorStoreIndex.from_documents(docs, service_context=service_context)`:

The `from_documents()` method of `VectorStoreIndex` is called, passing in the `docs`
list and the `service_context`. This creates an instance of `VectorStoreIndex` and
populates it with the documents and their vector representations.

5. `return index`: 

The `index` object, which represents the populated
`VectorStoreIndex`, is returned from the `load_data()` function
''')

st.divider()
st.subheader("4. Initializing the Chat Engine")

st.code(r'''
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
''')

st.markdown("*This line initializes the chat engine*")
st.markdown('''
* `index` is the index we created in the previous step

* `as_chat_engine()` is a method of the `VectorStoreIndex` class that creates a chat engine from the index.
Basically all the Data which we had transformed into vectors in the previous step is now being used to create a chat engine.

* `chat_mode="condense_question"` This mode condenses the user's question(or prompt) into a shorter
form, which can be useful for more concise interactions.

* `verbose=True` If this Parameter is set to True then the chat engine provides additional
information and feedback during the conversation process.
''')

st.divider()
st.subheader("5. Starting the Chat")
st.code(r'''
while True:
    prompt = input("Your question: ")
    if not prompt:
        break
    # Generate a response
    response = chat_engine.chat(prompt)
    print("Assistant:", response.response)
''')
st.markdown("*This Marks the Start of the Chatbot*")

st.markdown('''
* `while True:` 

This is a loop that runs forever until the user enters a blank prompt. This allows us to have a conversation with the chatbot continously.

* `prompt = input("Your question: ")` 

This line takes the user's input and stores it in the `prompt` variable. This is essentially the same as typing a prompt into the chat box on the ChatGPT website.

* `if not prompt:` 

This condition checks if the user has entered an empty prompt
(by pressing Enter without typing anything). If the prompt is empty, the loop is exited, and
the conversation ends

* `response = chat_engine.chat(prompt)` 

This line sends the user's prompt to the chat
engine for processing. The chat engine generates a response based on the input and assigns
it to the `response` variable.


* `print("Assistant:", response.response)` 

This line prints the assistant's response to the
console, indicating that it is the assistant's turn to speak. The `response.response`
attribute contains the actual response generated by the chat engine.
''')

ColoredHeader(
    "Streamlit",
    description="Now we will be using Streamlit to make a web app out of this. Let's start with the Basics"
)

st.title("Text Elements")
st.divider()

st.subheader("1. Title")
with st.echo():
    st.title("**This** is how we can *add* `Title`") # similar to h1 in html
st.divider()

st.subheader("2. Subheader")
with st.echo():
    st.subheader('This is a subheader with a divider', divider='rainbow')
    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
    st.subheader("This is a **Bold Header**, This is an *Italic Header*" ) #  similar to h2 in html
st.divider()

st.subheader("3. Markdown")
with st.echo():
    st.markdown("This is a Markdown, <mark>highlighted using html</mark>, <del>Cut out</del>", unsafe_allow_html=True) # to display any markdown element
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)
st.divider()

st.subheader("4. Write")
with st.echo():
    st.write("This is a Write, It displays any text element based on its data type") # to display any text element, will update based on the type of element
st.divider()

st.subheader("5. Latex")
with st.echo():
    st.latex(r"e^{i\pi} + 1 = 0") # to display any latex element
st.divider()

st.subheader("6. Caption")
with st.echo():
    st.caption('This is a string that explains something above.')
    st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


