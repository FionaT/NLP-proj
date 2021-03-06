# Evaluation

####Get our tags set
Just read the first column of tags_keywords.txt
* input_file: tags_keywords.txt
* out_file: our_tags_set
    
####Get yelp tags set
Read all attributes mentioned in yelp's businesses, find the union set of these attributes.
* input_file: yelp_academic_dataset_business.json
* code: get_all_yelp_tags.py
* out_file: Yelp_tags_set.txt
    
Currently, all attributes mentioned in Yelp are in the Yelp_tags_set.txt file.

####Get overlap between yelp tags set and our tags set
The result overlap tags set will be the valid set for calculating precision and recall.
* input_file: our_tags_set & Yelp_tags_set.txt
* code: get_overlap_tags.py
* out_file: overlap_tags.txt
    
#### Get our tags for each business: 
Compare the negative count and positve count from partfeature-1 file of each tag, if the positive count is larger than negative count, then we will add this tag to this business. Output the tags generated by our system in the form of (business_id, tags1, tags2, tags3 ... tagsN). 

* input_file: partfeature-1
* code: get_our_tags.py
* out_file: business_tags.txt

#### Get yelp's attributes for each business: 
Output the attribute tags from yelp public data also in the form of (business_id, tags1, tags2, tags3 ... tagsN). 

* input_file: yelp_academic_dataset_business.json
* code: get_business_attributes.py
* out_file: business_attributes.txt

####Compare our tags for each business and yelp's attributes for each business

First of all, the businesses' order generated by our system is different from yelp's businesses order, so we will map each business id to its index in yelp data first. Then we start reading the business_tags.txt file (which shows each business's tags generated by our system), for each business we compare its tags generated by us and its attributes marked in Yelp data, and caculate the precision and recall for each business. At the end, we sum up all precision and recall and caculate the average value.

* input_file: 
        overlap_tags.txt & business_tags.txt & business_attributes.txt
* code: compare.py
* out_file: compare.txt