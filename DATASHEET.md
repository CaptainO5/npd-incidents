# Norman PD 

## Motivation

1. **For what purpose was the dataset created?** *(Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.)*
    
    This dataset was created as part of an assignment, aiming to learn data augmentation processes.


1. **Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?**
    
    This dataset was created by Suraj Kolla. At the time of creation, Suraj was a graduate student at the University of Florida (UF).


1. **Who funded the creation of the dataset?** *(If there is an associated grant, please provide the name of the grantor and the grant name and number.)*
    
    None.


1. **Any other comments?**
    
    None.





## Composition


1. **What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?** *(Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.)*
    
    Each instance is an incident that occured in Norman OK, reported by the local police department. 


2. **How many instances are there in total (of each type, if appropriate)?**
    
    There is an incident report for each day, each report consits of around 400 instances of the incidents. The incidents range from crimes, 911 calls to hospital emergencies.


3. **Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** *(If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).)*
    
    It is a sample of all possible documents. It is not intended to be representative.


4. **What data does each instance consist of?** *(``Raw'' data (e.g., unprocessed text or images)or features? In either case, please provide a description.)*
    
    Each instance consists of the following features.

    `Day of Week` (integer): The day of week is a numeric value in the range 1-7 starting from Sunday.

    `Time of Data` (integer): The time of data is a numeric code from 0 to 23 describing the hour of the incident.

    `Weather` (integer): Represents the weather at the time and location of the incident. The weather is determined by the WMO CODE. The code is an integer that represents a weather position.

    `Location Rank` (integer): Rank of the location, based on the number of occurrences. The ties are preserved; locations with same frequency are given the same rank, the next most frequent location would be ranked as if the previous locations are ranked continuosly.

    `Side of Town` (String): The side of town is one of the eight items {N, S, E, W, NW, NE, SW, SE}. Side of town is determined by approximate orientation of the center of town (35.220833, -97.443611). The Center itself is assigned E.

    `Incident Rank` (integer): Similar to location rank, ranked based on the frequency of incidents, while also preserving the ties.

    `Nature` (String): The Nature is the direct text of the Nature from the source record, representing the category of the nature of the incident.

    `EMSSTAT` (boolean): This is a boolean value that is True in two cases; first, if the Incident ORI was EMSSTAT or if the subsequent record or two contain an EMSSTAT at the same time and locaton.


5. **Is there a label or target associated with each instance? If so, please provide a description.**
    
    Nature could be a potential target.


6. **Is any information missing from individual instances?** *(If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.)*
    
    In some cases, the location details are not accurately documented in the source, for which I am defaulting them to the noramn town center.

7. **Are relationships between individual instances made explicit (e.g., users' movie ratings, social network links)?** *( If so, please describe how these relationships are made explicit.)*
    
    No

8. **Are there recommended data splits (e.g., training, development/validation, testing)?** *(If so, please provide a description of these splits, explaining the rationale behind them.)*
    
    None


9. **Are there any errors, sources of noise, or redundancies in the dataset?** *(If so, please provide a description.)*
    
    Center of the town location could be redundant because that was set as default for unknown or bad location choices.


10. **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?** *(If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.)*
    
    It is dependent on the norman pd incident report summaries, they change every month but there is always data worth of two months available on their website.


11. **Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** *(If so, please provide a description.)*
    
    No; all raw data in the dataset is from a public source.


12. **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** *(If so, please describe why.)*
    
    None of that serious. nature


13. **Does the dataset relate to people?** *(If not, you may skip the remaining questions in this section.)*
    
    Yes in a way.


14. **Does the dataset identify any subpopulations (e.g., by age, gender)?** *(If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.)*
    
    No.


15. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** *(If so, please describe how.)*
    
    No.


16. **Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** *(If so, please provide a description.)*
    
    No. Nothing that can relate to an individual.


17. **Any other comments?**
    
    None.





## Collection Process


1. **How was the data associated with each instance acquired?** *(Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.)*
    
    The data was all downloaded directly from associated webpage. Used geocoder and historical weather apis to document some of the details.


1. **What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?** *(How were these mechanisms or procedures validated?)*
    
    Geocodio API for geocoding. Historical weather API for getting weather codes. Normal pandas functionalities for other variables.

1. **If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?**
    
    Samples are of user interst, they can send any number of incident report files to get the data.


1. **Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?**
    
    All collection and augmentation was done by the author.


1. **Over what timeframe was the data collected?** *(Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)?  If not, please describe the timeframe in which the data associated with the instances was created.)*
    
    Early April, 2024.


1. **Were any ethical review processes conducted (e.g., by an institutional review board)?** *(If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.)*
    
    None.


1. **Does the dataset relate to people?** *(If not, you may skip the remaining questions in this section.)*
    
    Yes; the incdents are kind of related, but the dataset does not identinfy any individuals.


1. **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?**
    
    Other sources: Norman PD website.


1. **Were the individuals in question notified about the data collection?** *(If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.)*
    
    No.


1. **Did the individuals in question consent to the collection and use of their data?** *(If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.)*
    
    No. All documents are public.

1. **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** *(If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).)*
    
    N/A.


1. **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?** *(If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.)*
    
    No. 


1. **Any other comments?**
    
    None.





## Preprocessing/cleaning/labeling


1. **Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** *(If so, please provide a description. If not, you may skip the remainder of the questions in this section.)*
    
    Yes; the data are augmented and to get only the required information.


1. **Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?** *(If so, please provide a link or other access point to the "raw" data.)*
    
    No.


1. **Is the software used to preprocess/clean/label the instances available?** *(If so, please provide a link or other access point.)*
    
    All the software are public APIs.


1. **Any other comments?**
    
    None.





## Uses


1. **Has the dataset been used for any tasks already?** *(If so, please provide a description.)*
    
    None yet.


1. **Is there a repository that links to any or all papers or systems that use the dataset?** *(If so, please provide a link or other access point.)*
    
    No.


1. **What (other) tasks could the dataset be used for?**
    
    The dataset could possibly be used for developing or testing systems for predicting future incidents. 


1. **Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** *(For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other undesirable harms (e.g., financial harms, legal risks)  If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?)*
    
    None.


1. **Are there tasks for which the dataset should not be used?** *(If so, please provide a description.)*
    
    None.


2. **Any other comments?**
    
    None.




## Distribution


1. **Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?** *(If so, please provide a description.)*
    
    None


1. **How will the dataset will be distributed (e.g., tarball  on website, API, GitHub)?** *(Does the dataset have a digital object identifier (DOI)?)*
    
    N/A


1. **When will the dataset be distributed?**
    
    No.


1. **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** *(If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.)*
    
    MIT License, free to use.


1. **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** *(If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.)*
    
    Not to our knowledge.


1. **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** *(If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.)*
    
    Not to our knowledge.


1. **Any other comments?**
    
    None.





## Maintenance


1. **Who is supporting/hosting/maintaining the dataset?**
    
    The code to create the dataset is hosted on github.


1. **How can the owner/curator/manager of the dataset be contacted (e.g., email address)?**
    
    E-mail address: n.kolla@ufl.edu.


1. **Is there an erratum?** *(If so, please provide a link or other access point.)*
    
    No

1. **Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances')?** *(If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?)*
    
    No


1. **If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** *(If so, please describe these limits and explain how they will be enforced.)*
    
    No


1. **Will older versions of the dataset continue to be supported/hosted/maintained?** *(If so, please describe how. If not, please describe how its obsolescence will be communicated to users.)*
    
    No


1. **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** *(If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.)*
    
    Errors may be submitted via the issues page on github


1. **Any other comments?**
    
    None.

