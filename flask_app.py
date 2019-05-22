from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SearchForm, TechmemeForm
from reddit_search import search_post
from news import verge, techcrunch
from techmeme_aggregator import techmeme

app = Flask(__name__)
app.config['SECRET_KEY'] = '791628bb0b13ce0c676dfde'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/reddit_search', methods= ['GET', 'POST'])
def reddit_search():
    form = SearchForm()
    if form.validate_on_submit():
        searched_term = form.search.data
        time_filter = form.time_select.data
        data = search_post(searched_term, time_filter)
        if data:
            flash("Search results for '{}'".format(searched_term), 'success')
            return render_template('reddit_search.html', form= form, data= data)
        else:
            flash("No results were found for '{}'".format(searched_term), 'danger')
       
    return render_template('reddit_search.html', form= form, data= None)
    

@app.route('/news')
def news():
    verge_data = verge()
    techcrunch_data = techcrunch()
    if verge_data and techcrunch_data:
        flash("News from verge and techcruch.", 'success')
        return render_template('news.html', verge_data= verge_data, techcrunch_data= techcrunch_data)

    return render_template('news.html', verge_data= None, techcrunch_data= None)


@app.route('/techmeme_search', methods= ['GET', 'POST'])
def techmeme_search():
    form = TechmemeForm()
    if form.validate_on_submit():
        searched_term = form.search.data
        result = techmeme(searched_term)
        if result:
            flash("Search results for '{}'".format(searched_term), 'success')
            return render_template('techmeme_aggregator.html', result= result, form= form)
        else:
            flash("No results were found for '{}'".format(searched_term), 'danger')

    return render_template('techmeme_aggregator.html', result= None, form= form)


if __name__ == "__main__":
    app.run(debug=True)
    