import streamlit as st
import pickle


@st.cache_data()
def predict_sentiment(_model, tweet):
    prediction = _model.predict([tweet])
    return prediction[0]


@st.cache_data()
def load_model():
    return pickle.load(open("twitter_sentiment.pkl", 'rb'))

def show_image(sentiment):
    image_path = ""
    if sentiment == "Positive":
        image_path = r"positive.jpg"
    elif sentiment == "Negative":
        image_path = r"negative.jpg"
    elif sentiment == "Neutral":
        image_path = r"neutral.jpg"
    else:
        image_path = r"irrelevant.jpg"

   
    st.image(image_path, caption="Sentiment: " + sentiment, width=200)


def check_tweets():
    
    st.title("Check Your Tweets")
    
    
    model = load_model()

    
    tweet = st.text_input("Enter your tweet")

    
    if st.button("Predict"):
        
        prediction = predict_sentiment(model, tweet)
        
        
        st.session_state.prediction = prediction
        
        
        st.write("Predicted sentiment is:", prediction)
        show_image(prediction)


def model_build():
    
    st.title("Model Build")

    
    if st.button("Show Images"):
        
        st.subheader("Pie Chart of Sentiments")
        
        pie_chart_image = "sentiment.jpg"

        st.image(pie_chart_image, use_column_width=True)

        
        st.subheader("Wordclouds")
        
        positive_wordcloud_image =  r"positive-wc.jpg"
        negative_wordcloud_image = r"negative-wc.jpg"
        neutral_wordcloud_image = r"neutral-wc.jpg"
        irrelevant_wordcloud_image = r"irrelavent-wc.jpg"

       
        col1, col2 = st.columns(2)
        with col1:
            st.image(positive_wordcloud_image, caption="Positive", use_column_width=True)
            st.image(negative_wordcloud_image, caption="Negative", use_column_width=True)
        with col2:
            st.image(neutral_wordcloud_image, caption="Neutral", use_column_width=True)
            st.image(irrelevant_wordcloud_image, caption="Irrelevant", use_column_width=True)


def main():
    
    st.markdown("""
    <style>

    .options {
        display: flex;
        justify-content: center;
    }
    .option {
        margin: 0 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown("<h1 class='title'>Twitter Sentiment Analysis</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("<h3 class='option'>Analysis</h3>", unsafe_allow_html=True)

    
    selected_option = st.sidebar.radio("Navigation", ["Check Your Tweets", "Model Build"])

    
    if selected_option == "Check Your Tweets":
        check_tweets()
    elif selected_option == "Model Build":
        model_build()


if __name__ == "__main__":
    main()
