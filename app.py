{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'scrape'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-d6b377498547>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mflask\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mFlask\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrender_template\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpymongo\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mscrape\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# create instance of Flask app\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'scrape'"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template\n",
    "import pymongo\n",
    "import scrape\n",
    "\n",
    "# create instance of Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# create mongo connection\n",
    "client = pymongo.MongoClient()\n",
    "db = client.mars_db\n",
    "collection = db.mars_data_entries\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    mars_data = list(db.collection.find())[0]\n",
    "    return  render_template('index.html', mars_data=mars_data)\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def web_scrape():\n",
    "    db.collection.remove({})\n",
    "    mars_data = scrape.scrape()\n",
    "    db.collection.insert_one(mars_data)\n",
    "    return  render_template('scrape.html')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
