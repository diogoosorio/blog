----
category: PHP
create_date: 2012-05-27
description: This is a quick guide that aims to explain the necessary steps to get Solr up and running in 15 minutes. I'll be using Ubuntu throughout the entry.
title: Quick Solr Tutorial - Up and Running in 15 Minutes (Ubuntu version)
keywords: solr, solr tutorial, solr ubuntu, solr debian, solr quick guide, solr guide, solr php
slug: quick-solr-tutorial-php-ubuntu-debian
----

This week I've been toying around with **[Apache's
Solr](lucene.apache.org/solr/)**. For those who are unfamiliar with the
technology, **Solr** is a search platform that enables you to query and
retrieve information. _"That's not what any traditional RDBMS_ does?" - you
might ask. Well kinda... but not quite.

You see **Solr** is optimized to preform text searches and does it [remarkably
fast](http://jayant7k.blogspot.pt/2006/06/benchmarking-results-of-mysql-
lucene.html). It's not an alternative for whatever way you use to persistently
store your data (MySQL, MSSQL, NoSQL, ...), but if you're facing certain
requriements (like the ability to "search" for a given string througouht large
ammounts of data), **Solr** becomes a solid complementary platform that you
can use to build your application.

For a more info, consider giving a look at ["Why use
Solr?"](http://wiki.apache.org/solr/WhyUseSolr) and at [Solr's
features](lucene.apache.org/solr/).

&nbsp_place_holder;

### Step 1 - Installing Solr

So first things first, lets get Solr up and running in our machine. I'm using
**Ubuntu** and __**Apt-Get**. Please note that Solr is written in Java and
requires a servlet container. I'll be using
[**Jetty**](http://jetty.codehaus.org/jetty/) just because... well everything
worked flawlessly on the first try (I'm lazy and I value those kind of
things).

    
    sudo aptitude install solr-common solr-jetty

At this point you should be able to point your browser to
[http://localhost:8080/solr/](http://localhost:8080) and actually see
something.

&nbsp_place_holder;

### Step 2 - How to Play With Solr

So before we continue lets stop for a minute and talk about how this thing
works. I'm also starting to get the hang of things, so if you find any
incorrection shoot me an email.

Solr enables you to add and retrieve content through HTTP requests and **XML**
is the "de facto" way to communicate with Solr (although
**[JSON](http://wiki.apache.org/solr/SolJSON)** and possibly other notations
can be used).

To add/delete some data from Solr, you send a POST request to the server. If
you want to preform a search query, you issue a GET request (more details
about this bellow).

Internally the data is indexed as "Documents". A document may contain a number
of fields and typically it would also include an unique identifier. The
structure of the document is defined on the **schema.xml** file.****

So lets imagine that we are building a recipes website and we want to give the
possibility for our visitors to preform a "search" for any term on our
website. Every recipe would be a "document" with the following fields -
**Title**, **Ingr****edients**, **Prepara****tion Time **(in minutes) and
******Instructions** (the recipe itself).

&nbsp_place_holder;

### Step 3 - Building the Schema.xml

As I've noted before, the **schema** file is where you actually inform Solr
about what it can be indexed. You can find this file within the
_/etc/solr/conf__ _folder.

The file is thoroughly commented, so if you want to spend some time reading
it, please do. For the sake of this entry's length, I'll keep it to the
essential.

    
    <?xml version="1.0" encoding="UTF-8" ?>
    <schema name="recipes" version="1.2">
    	<types>
    		<fieldType name="string" class="solr.StrField" sortMissingLast="true" omitNorms="true"/>
    		<fieldType name="boolean" class="solr.BoolField" sortMissingLast="true" omitNorms="true"/>
    		<fieldtype name="binary" class="solr.BinaryField"/>
    		<fieldType name="int" class="solr.TrieIntField" precisionStep="0" omitNorms="true" positionIncrementGap="0"/>
    		<fieldType name="float" class="solr.TrieFloatField" precisionStep="0" omitNorms="true" positionIncrementGap="0"/>
    		<fieldType name="long" class="solr.TrieLongField" precisionStep="0" omitNorms="true" positionIncrementGap="0"/>
    		<fieldType name="double" class="solr.TrieDoubleField" precisionStep="0" omitNorms="true" positionIncrementGap="0"/>
    		<fieldType name="date" class="solr.TrieDateField" omitNorms="true" precisionStep="0" positionIncrementGap="0"/>
    		<fieldType name="text" class="solr.TextField" positionIncrementGap="100">
    		  <analyzer type="index">
    		    <tokenizer class="solr.WhitespaceTokenizerFactory"/>
    		    <filter class="solr.StopFilterFactory"
    		            ignoreCase="true"
    		            words="stopwords.txt"
    		            enablePositionIncrements="true"
    		            />
    		    <filter class="solr.WordDelimiterFilterFactory" generateWordParts="1" generateNumberParts="1" catenateWords="1" catenateNumbers="1" catenateAll="0" splitOnCaseChange="1"/>
    		    <filter class="solr.LowerCaseFilterFactory"/>
    		    <filter class="solr.SnowballPorterFilterFactory" language="English" protected="protwords.txt"/>
    		  </analyzer>
    		  <analyzer type="query">
    		    <tokenizer class="solr.WhitespaceTokenizerFactory"/>
    		    <filter class="solr.SynonymFilterFactory" synonyms="synonyms.txt" ignoreCase="true" expand="true"/>
    		    <filter class="solr.StopFilterFactory"
    		            ignoreCase="true"
    		            words="stopwords.txt"
    		            enablePositionIncrements="true"
    		            />
    		    <filter class="solr.WordDelimiterFilterFactory" generateWordParts="1" generateNumberParts="1" catenateWords="0" catenateNumbers="0" catenateAll="0" splitOnCaseChange="1"/>
    		    <filter class="solr.LowerCaseFilterFactory"/>
    		    <filter class="solr.SnowballPorterFilterFactory" language="English" protected="protwords.txt"/>
    		  </analyzer>
    		</fieldType>
    	</types>
    
    	<fields>
    		<field name="id" type="string" indexed="true" stored="true" required="true" />
    		<field name="title" type="string" indexed="true" stored="true" />
    		<field name="ingredients" type="string" multiValued="true" indexed="true" stored="true" />
    		<field name="instructions" type="text" indexed="true" stored="true" />
    		<field name="text" type="text" indexed="true" stored="false" multiValued="true" />
    	</fields>
    	
    	 <uniqueKey>id</uniqueKey>
    	 <defaultSearchField>text</defaultSearchField>
    	 <solrQueryParser defaultOperator="AND"/>
    	 
    	 <copyField source="title" dest="text"/>
    	 <copyField source="instructions" dest="text" />
    	 <copyField source="ingredients" dest="text" />
    </schema>

Disregard the **<types>** node, it falls out of the scope of this article.
What we're interested in is the **<fields****>** node. Here is where we define
what Solr should be expecting from us - a field named **id**, **t****itle**,
**ingredients**, **instruc****tions** and **text**.

Wait **text**, what's that? If you scroll down a bit more, you'll find that
we've defined that exact field as the **defaultSearchField**. This means that
by default, Solr will probe the contents of that field to find whatever we're
looking for.

At the bottom of the schema you'll find this:

    
    <copyField source="title" dest="text"/>
    <copyField source="instructions" dest="text" />
    <copyField source="ingredients" dest="text" />

This basically means that anything that you insert on the **title**,
**instructions** and **ingredients** will get copied into the **text** field.
In pratical terms (and on this example), the **text **field will contain
pretty much everything you'll need to preform any kind of search (a term on
the instructions, an ingredient, ...).

This fact doesn't mean that you can't query the specific fields on their own
(you can), it just makes the search query simpler if you want to quickly
search for a recipe.

So what about the attributes on each of the **field** nodes? Here's a quick
explanation:

  1. **name: **the name of the field, duh!
  2. **type**: the data type that the field will contain. The data type must be defined within the **types** node.
  3. **indexed**: should this field be "queryable"? Do you expect to preform a search against it?
  4. **stored: **should the field's content be outputed when you preform a query?
  5. **multiValued:** will the field accept multiple entries (ex. the ingredients field)
  6. **required**: is the field required?

&nbsp_place_holder;

### Step 3 - Inserting a Document

After storing your **schema.xml** and restarting **Jetty**, you should be
ready to actually start storing / querying data from Solr.

To index a new document on Solr, we'll make a **HTTP POST** request to the
servlet, passing along the information that we want to store in a XML format.
Here's the actual recipe we're trying to insert:

    
    <add>
        <doc>
            <field name="id">1</field>
            <field name="title">French Fries</field>
            <field name="ingredients">Potatoes</field>
            <field name="ingredients">Olive Oil</field>
            <field name="ingredients">Salt</field>
            <field name="instructions">
                Cut the french fries with mandoline or french fry cutter 1/4-inch strips. Heat a saucepan or stock pot (at least 2 gallon capacity) with the oil about 250 degrees (use a thermometer to gauge). Add the french fries and cook, stirring to avoid clumping together, about 3 minutes, until soft but not mushy. Remove with a mesh strainer and drain onto paper towels. Turn heat to high and heat oil to 350 degrees. At the last minute before serving plunge the fries into the oil and cook until golden brown. Remove from oil, drain onto towels and season with salt to taste.
            </field>
        </doc>
        <commit />
        <optimize />
    </add>

Save the document as _french_fries.xml_ and we'll use cURL to make the
request:

    
    curl -d @french_fries.xml -H "Content-Type: text/xml" http://localhost:8080/solr/update/

If everything went as expected, you should receive a reply that looks
something like this:

    
    <?xml version="1.0" encoding="UTF-8"?>
    <response>
        <lst name="responseHeader">
            <int name="status">0</int>
            <int name="QTime">343</int>  
        </lst>
    </response>

You can now take a look at Solr's admin panel to make sure the document was
actually inserted. To do so, point your browser here: [http://localhost:8080/s
olr/admin/stats.jsp](http://localhost:8080/solr/admin/stats.jsp)

You should see that the **numDocs **value is **1**:

![](../../public/images/blog/blog/solr1.jpg)

&nbsp_place_holder;

&nbsp_place_holder;

### Step 4 - Querying Solr

So now that you actually have something to search for on Solr, you can
actually query and find what you're looking for.

Again for this entrie's length sake, I won't go very deep about the query
syntax (to be perfectly honest I'm also learning it), but from what I've
figured out so far, these are the most [common query
parameters](http://wiki.apache.org/solr/CommonQueryParameters):

  * **q**: your main query.
  * **start**: this would be the equivalent of the "offset" value on a SQL query
  * **rows**: this would b the equivalent of the "limit" value on a SQL query
  * **fq: **the filter query conditionates the documents that can be returned, without affecting the results scores.
  * **fl**: limits the fields that get returned by the query

Some examples (remember that the queries are made issuing a GET request
against Solr's servlet):

  * [http://localhost:8080/solr/select/?q=fries](http://localhost:8080/solr/select/?q=fries) - will search for a recipe who has the term "fries" within the text field  
  

  * [http://localhost:8080/solr/select/?q=fries AND ingredients:Salt](http://localhost:8080/solr/select/?q=fries%20AND%20ingredients:Salt%20) - will search for a recipe with the term "fries" on the text field and who has an ingredient named "Salt"  
  

  * [http://localhost:8080/solr/select/?q=*:*&rows=200](http://localhost:8080/solr/select/?q=*:*&rows=200) - return the first 200 recipes

For more information regarding Solr's query syntax, take a look at this [Wiki
article](http://wiki.apache.org/solr/SolrQuerySyntax). A typical successfull
response from Solr would look something like this:

    
    <?xml version="1.0" encoding="UTF-8"?>
    <response>
        <lst name="responseHeader">
            <int name="status">0</int>
            <int name="QTime">36</int>
            <lst name="params">
                <str name="q">*:*</str>
            </lst>
        </lst>
        <result name="response" numFound="1" start="0">
            <doc>
                <str name="id">1</str>
                <arr name="ingredients">
                    <str>Potatoes</str>
                    <str>Olive Oil</str>
                    <str>Salt</str>
                </arr>
                <str name="instructions">			Cut the french fries with mandoline or french fry cutter 1/4-inch strips. Heat a saucepan or stock pot (at least 2 gallon capacity) with the oil about 250 degrees (use a thermometer to gauge). Add the french fries and cook, stirring to avoid clumping together, about 3 minutes, until soft but not mushy. Remove with a mesh strainer and drain onto paper towels. Turn heat to high and heat oil to 350 degrees. At the last minute before serving plunge the fries into the oil and cook until golden brown. Remove from oil, drain onto towels and season with salt to taste.		</str>
                <str name="title">French Fries</str>
            </doc>
        </result>
    </response>
    

&nbsp_place_holder;

