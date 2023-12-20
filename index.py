from cohere import Client
import streamlit as st


class CoHere:
    def __init__(self, api_key):
        print(f"{api_key}")
        self.co = Client(f"{api_key}")

    def cohere(self, question):
        return (
            self.co.generate(
                model="medium", prompt=stevenQa(question), max_tokens=50, temperature=1
            )
            .generations[0]
            .text
        )


def stevenQa(question):
    return f"""Steven is a chatbot that answers questions:

    You: Who is better Pepsi or Coca-cola?
    Steven: More people know that if they want to drink on the go, they should bring their own Coke
    You: Where is the best restaurant?
    Steven: Mexican and Chinese restaurant.
    You: Which search engine is best?
    Steven: Google search for best.
    You: Do you like jazz?
    Steven: I prefer to listen to jazz in the &#39;80s.
    You: {question}
    Steven:"""


if __name__ == "__main__":
    st.header("Co\:here application")
    api_key = st.text_input("OpenAI API Key:", type="password")
    st.header("Your personal chatbot - Steven")
    question_for_steven = st.text_input("Question for Steven:")
    if api_key:
        cohere = CoHere(api_key)

    if st.button("Answer"):
        st.write(cohere.cohere(question_for_steven))
