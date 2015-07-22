#!/usr/bin/env python
import elasticsearch

def home()  :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='cities', body={
        'title': 'home',
        'url': 'home',
        'text': 'GOTOPAWS ADOPT A FRIEND TODAY!',
    })

def pets() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Pets',
        'url': 'pets',
        'text': 'Search for and find your perfect companion. Rescue a pet and give them a forever home. Picture Name Age Sex Size Breed Shelter City pets    Trixie Bell Senior  F   S   Chihuahua   TX1148  Austin pets    Amigo   Adult   M   S   Chihuahua   TX1148  Austin pets    Lillipup    Baby    F   S   Chihuahua   TX1148  Austin pets    Turner  Young   M   S   Chihuahua   TX1148  Austin pets    Nico    Young   F   S   Chihuahua   TX1148  Austin pets    Cody    Adult   M   S   Chihuahua   TX1148  Austin pets    Vivian - Courtesy Listing   Young   F   M   Domestic Short Hair TX1148  Austin pets    Prissy  Adult   F   S   Chihuahua   TX1148  Austin pets    Skeeter Adult   M   S       TX1148  Austin pets    Georgia Senior  F   S   Pomeranian  TX1148  Austin pets    VINCE   Adult   M   L   Shar Pei    TX295   San Antonio pets    FERLIN  Adult   M   L   Catahoula Leopard Dog   TX295   San Antonio pets    ANISHA  Adult   F   M   Labrador Retriever  TX295   San Antonio pets    WHISPER Senior  F   M   Cattle Dog  TX295   San Antonio pets    SUZIE   Adult   F   L   Shepherd    TX295   San Antonio pets    KODIAK  Adult   F   M   Siberian Husky  TX295   San Antonio pets    FROSTIE Young   F   M   Hound   TX295   San Antonio pets    PETRA   Young   F   M   Retriever   TX295   San Antonio pets    MARLOW  Senior  M   L       TX295   San Antonio pets    PRESLEY Senior  M   M   Terrier TX295   San Antonio pets    Nutmeg  Senior  F   M   Basset Hound    TX1051  Houston pets    Scout   Young   M   M   Basset Hound    TX1051  Houston pets    Milo    Senior  M   M   Basset Hound    TX1051  Houston pets    Sherman III Young   M   M   Basset Hound    TX1051  Houston pets    Huntley Senior  M   M   Basset Hound    TX1051  Houston pets    Rufus   Senior  M   M   Basset Hound    TX1051  Houston pets    Albert  Senior  M   XL  Basset Hound    TX1051  Houston pets    Eva Young   F   M   Basset Hound    TX1051  Houston pets    Remy    Senior  M   M   Basset Hound    TX1051  Houstonpets    Buster  Adult   M   M       TX1283  Houston pets    Annabelle   Adult   F   L   Collie  TX1283  Houston pets    Skylar  Adult   F   L   Collie  TX1283  Houston pets    Connor  Young   M   L   Collie  TX1283  Houston pets    Rolo    Young   M   M       TX1283  Houston pets    Boots   Adult   M   L   Collie  TX1283  Houston pets    Marshall    Young   M   L   Collie  TX1283  Houston pets    Kermit  Adult   M   S   Shetland Sheepdog Sheltie   TX1283  Houston pets    Lady Di & Prince Charles    Adult   F   L   Collie  TX1283  Houston pets    Jake    Young   M   M   Australian Cattle Dog (Blue Heeler) TX1283  Houston pets    Hazel   Adult   F   M   Calico  CA1061  San Francisco pets    Nibbler Adult   M   L   Tabby - Brown   CA1061  San Francisco pets    Minnie  Adult   F   S   Tabby   CA1061  San Francisco pets    Purr    Adult   F   S       CA1061  San Francisco pets    Daphne  Adult   F   S       CA1061  San Francisco pets    Maverick    Adult   M   L       CA1061  San Francisco pets    Emerald aka Emmy    Young   F   S   Domestic Short Hair-black   CA1061  San Francisco pets    Mittens Senior  F   M       CA1061  San Francisco pets    Leila   Senior  F   L   Domestic Short Hair-black and white CA1061  San Francisco pets    Sammy Sweet Cheeks  Adult   M   M       CA1061  San Francisco pets    Molly   Young   F   S   Persian CA1063  San Francisco pets    Derek   Young   M   M   Himalayan   CA1063  San Francisco pets    Lady    Young   F   M   Persian CA1063  San Francisco pets    Lisa    Young   F   M   Persian CA1063  San Francisco pets    Ginger  Adult   F   M       LA204   New Orleans pets    Honey   Adult   F   S       LA204   New Orleans pets    Kermit  Adult   M   L   Domestic Short Hair - orange and white  LA204   New Orleans pets    Thelma  Adult   F   S       LA204   New Orleans pets    Daphy   Young   F   L   Labrador Retriever  LA204   New Orleans pets    Joy Young   F   S   Poodle  LA204   New Orleans pets    Lt. Dan Baby    M   S       LA204   New Orleans pets    Mama D  Adult   F   L   Australian Cattle Dog (Blue Heeler) LA204   New Orleans pets    Sergio  Adult   M   L       LA204   New Orleans pets    Romeo   Adult   M   S   Chihuahua   LA204   New Orleans pets    Cayenne Adult   M   XL      LA305   New Orleans pets    Thomas  Adult   M   L       LA305   New Orleans pets    Kayle   Adult   F   M       LA305   New Orleans pets    STAR    Adult   M   L       LA305   New Orleans pets    Angelina    Adult   F   M       LA305   New Orleans pets    Brad    Adult   M   M       LA305   New Orleans pets    Sampson Adult   M   XL      LA305   New Orleans pets    Moine (indoor outdoor)  Adult   F   M   Tortoiseshell   LA305   New Orleans pets    Valinda Adult   F   XL  Siamese LA305   New Orleans pets    Sam Elliott Young   M   L   Tabby - Grey    LA305   New Orleans',
    })

def pet_1() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Trixie Bell',
        'url': 'id23293772',
        'text': 'Age: Senior Sex: F Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Age: 8-10 years Weight: 5 lbsBio story coming soon!**Please note that Trixie is undergoing a slow heartworm treatment due to being extensively infected with them. As this treatment is a lengthy process, we are accepting applications for a \'foster to adopt\' situation where an adopter can foster her through treatment which will be covered financially by the group. Please contact us for more details**Adoption fee is $200. If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application. The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_2() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Amigo',
        'url': 'id24306492',
        'text': 'Age: Adult Sex: M Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Amigo is a Courtesy Posting, which means that he is not in our rescue group, but we are posting him for a member of the public who is trying to find him a new home:This little guy was on the side of the road and started chasing my truck as I passed by. He was almost hit by oncoming traffic so I had to stop and pick him up. He\'s definitely an older chihuahua mix but thankfully, neutered. He needs a little TLC but overall, he is very sweet. He really doesn\'t pay any mind to my dogs. He is crate trained but I have yet to determine if he is completely housebroken. He just wants attention and will occasionally cry in the kennel when I have to leave for work. He walks well on lead but I don\'t think he knows any commands. Please Contact: Brandie for more information: freebsrn@aol.comAdoption fee is $125. If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_3() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Lillipup',
        'url': 'id25816312',
        'text': 'Age: Baby Sex: F Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Age: 2 yearsWeight: 4 lbsLilipup is a smart, sweet and spunky little girl. She is both a a cuddler and a player, and can play all day long with her toys and foster siblings. Her sweet little eyes are a pretty brown, and she has an adorable prance when she is out on a walk. Lilli adjusts quickly to new environments despite sometimes being shy initially. She quickly learned the doggie door at multiple houses, and can be left in her crate overnight, though she would happily sleep with her new forever mom/dad/family. She can be apprehensive around some people, but if they let her be initially, she\'ll come around quickly. Lilli is good with children that would handle her well (she\'s very small), and rides well in the car, so she\'d be a great travel buddy. Adoption fee is $200. If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.' ,
    })

def pet_4() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Turner',
        'url': 'id27720354',
        'text': 'Age: Young Sex: M Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Age: 3-4 yrsWeight: 13 lbsTurner is a lovely young man. He\'s not terribly demanding, but if you offer him attention and affection, he will melt in your arms. He lives him a home with other dogs and gets along well with everyone, but we hope that in a forever home, Turner could be one of two/three dogs or possibly an only dog to receive the devotion he deserves. He was surrendered to the shelter by a family, and while he was around children in that home, it\'s clear that they actually spook him. In loud environments, you can tell that he is scared, but we\'ve noticed tremendous improvement recently in his comfort level with new people and environments. He walks well on leash when he knows and trusts you, but he can also lay down and freeze if frightened. An ideal home for Turner would be one with no young kids and a calmer environment. If someone where to continue to show him the positive sides to walks, public settings and just plain love from people - there\'s no doubt this guy will continue to flourish! Adoption fee is $200.If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_5() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Nico',
        'url': 'id31758203',
        'text': 'Age: Young Sex: F Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Age: 5 yearsWeight: 7 lbs Well hello world - here\'s Nico!  This spunky little gal is looking for a family to call her own, and she\'s ready to give you all the love she has.  There are two sides to Nico:  the calm snuggly girl and then the active playful girl.  She loves all people although she will initially bark at new people.  She\'s fostered in a home with other dogs and gets along very well with all of them.  She\'s also got 3 2-legged kids under the age of , and she gets along fabulously with them as well.  She has seriously never met a stranger.In the evenings, Nico likes to sit in your lap, on your shoulders, under the covers in your bed.  Basically, wherever you are, she would like to be...or she\'d like to be perched on the back of the couch to see where you may be from a distance.  She is crate-trained, and she\'s almost fully potty-trained.  She needs a little reminder when taken outside to do her business, but she\'s been doing fairly well.  She walks well on leash, so she may actually be used to a former apartment/condo lifestyle.For the side of Nico that is active, she would do well with a home that can offer her some physical activity and possibly some additional training.  She is highly treat/food motivated, which bodes well for increasing her bag of tricks.  Her foster family thinks she\'d actually make a great agility dog for a number of reasons including her ability to climb the ladder to the kids\' playscape to join them in the \'house\'.  She has tried to dig under a gate at her foster home twice now, so a home without a doggie door is an absolute must as she may be a flight risk.  Upon her first escape, she ran across the street and jumped into the driver seat of her neighbor who was leaving for work.  The neighbor was quite impressed with what a lover she is, but no one is impressed with her jail break antics :).Adoption fee is $200.If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_6() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Cody',
        'url': 'id31865520',
        'text': 'Age: Adult Sex: M Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Age: 5Weight: 4.5 lbs Cody is a sweet guy who needs a very special home. While we haven\'t been able to put all the pieces together on his puzzle prior to coming into our group from the shelter, we do know that he was shuffled around quite a bit over the years. He is very timid in nature, so if you\'re looking for a dog that will throw himself into your arms and greet you with lots of tail wags and kisses, he\'s not the guy for you. Any affection from Cody must be earned, and an adopter will have to be up for the challenge and the time involved in doing so. Having been with his foster family now for a couple months, he is still reserved and prefers only to cuddle up at bedtime. Cody will lay down on the floor about 10 feet from the couch if his foster mom is sitting down and cry for her, but when his foster mom goes to pick him up, he darts off :). He will follow her anywhere in the house to be where she is, but he\'s not interested in having her pick him up. If she does manage to catch him, he will sit nicely on the couch, sometimes in her lap or sometimes on the far end. At night-time, however, he will always go into his foster parents\' bedroom and will finally stand still to allow you to pick him up to put him on the bed. Unlike any chihuahua that his foster mom has ever had or fostered, he does not burrow under blankets! At night, he will sleep on the bed, and sometimes he\'ll get close enough to let his foster mom rest her hand on him. However, if you move in bed, he will scurry away again. He seems to view the bedroom as a safe spot and enjoys lounging on the bed while his family (2-legged parents and their 2-legged kids) get ready for work/school in the morning. He gets along well with the other dogs in his foster home although high energy dogs tend to scare him. Based on what we do know about his history, we do think he will likely always be a timid little man, so while a lot of work with him will likely gain a loyal and happy guy...he will likely never be an outgoing, social guy.Cody\'s teeth were severely neglected, but he received a dental where they removed 11 teeth. While under, we also had an x-ray done on his upper body area as he shows some discomfort/pain in the right shoulder area since arriving at his foster home. X-rays did not show anything abnormal, however. Cody was displaying shrieking episodes, and after witnessing an episode, the vet now believes he has been having focal seizures. The cause of the seizures is unknown, but based on his age, she believes it\'s likely a mild form of epilepsy. Cody is on a compounded prescription and has been since the middle of April, which is working! However, a potential adopter should note that these medications cost approximately $50/month ($600 annually), and he may be on them throughout the remainder of his life.Adoption fee is $200.If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_7() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Vivian - Courtesy Listing',
        'url': 'id32131434',
        'text': 'Age: Young Sex: F Size: M Breed: Domestic Short Hair Shelter: Small Chance Rescue City: Austin Hi,  my name is Vivian and I\'m a sweet loving kitty!  There\'s nothing I love more than to just lounge around and be pet and loved on!  And I am a purr box!!  I\'ve been spayed and now I\'m waiting for my forever home!I\'d be best in a home with no other cats so I\'m the queen bee and I get all the petting!!  For more info, contact Janet at 512-789-3467',
    })

def pet_8() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Prissy',
        'url': 'id32151349',
        'text': 'Age: Adult Sex: F Size: S Breed: Chihuahua Shelter: Small Chance Rescue City: Austin Age: Weight: Story coming soon!Adoption fee is $200.If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_9() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Skeeter',
        'url': 'id32301160',
        'text': 'Age: Adult Sex: M Size: S Breed: Shelter: Small Chance Rescue City: Austin Age: 3 yearsWeight: 10 lbsSkeeter is a 3 year old long haired chihuahua who loves attention and to give kisses to his \"person.\"  He is very sweet and great around other pets, but is very distrustful of strangers.  He becomes very anxious around them and can snap when overwhelmed, though he has never caused harm to anyone because many of his teeth were extracted.  He is also intimidated easily and will urinate submissively.  He needs to find a home with someone who is patient and loving and willing to work with him to build his confidence and minimize this submissive behavior.  Homes with children aren\'t recommended because he may feel overwhelmed.  The right person will get a loving and attentive fuzzy companion in him.Adoption fee is $200.If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_10() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Georgia',
        'url': 'id32416820',
        'text': 'Age: Senior Sex: F Size: S Breed: Pomeranian Shelter: Small Chance Rescue City: Austin Age: 12 yearsWeight: 15 lbsStory coming soon!  Adoption fee is $200.If you are interested in adopting, please read our Frequently Asked Questions before completing the adoption application.The application and general information can also be found at: www.smallchancerescue.com.',
    })

def pet_11() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'VINCE',
        'url': 'id31561986',
        'text': 'Age: Adult Sex: M Size: L Breed: Shar Pei Shelter: San Antonio Humane Society City: San Antonio Loving, smart, sweet, handsome, and curious all describe Vince perfectly. This adorable guy is a 6 year old Chinese Shar-Pei mix who cant wait to meet his new family. You will notice that even though Vince is excited to walk and explore, he does very well on a leash. When you are done walking, he is ready to show off his intelligent side  he already knows sit and down. Additionally, he is working on his puppy push-ups- where he goes from sit to down to sit - all with only one treat! Can you imagine what other tricks he will learn very quickly? And when he gets his treats, he takes them very gently. If you are looking for an exercise buddy, look no further, Vince is your dude! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd., visit SAhumane.org, or call (210) 226-7461.',
    })

def pet_12() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'FERLIN',
        'url': 'id31562035',
        'text': 'Age: Adult Sex: M Size: L Breed: Catahoula Leopard Dog Shelter: San Antonio Humane Society City: San Antonio Are you looking for a very friendly, smart, and fetching dog? If so, look no further, Ferlin is your man! He is a handsome 2 year old Catahoula Leopard mix who is ready for his forever family. When taken out for a walk, initially Ferlin will pull on his leash, but he quickly settles down. He already knows sit and will quickly learn more tricks. If sitting on command isnt enough for you, Ferlin will down and stay and responds to watch me and wait, especially when a yummy treat is presented. After exercising, playing, and learning new tricks, Ferlin is ready to love on his family. If you are ready for a smart and friendly boy, come to the SAHS and meet Ferlin - he will not disappoint! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. *** Adoption fees for dogs include: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd. or call (210) 226-7461.',
    })

def pet_13() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "ANISHA",
        "url": "id31562069",
        "text": "Age Adult Sex: F Size: M Breed: Labrador Retriever Shelter: San Antonio Humane Society City: San Antonio This loving Labrador Retriever mix is Anisha. She is a 6 year old gal who is full of energy. One of her favorite things to do involves going on daily walks and were happy to say that she does very well on a leash. Anisha has the cutest floppy ears, pretty brown eyes, and a soft salt and pepper coat. And get ready because one look at her smile and you will melt. Anisha is a lovebug, so if it is affection you are looking for, look no further, you have found it with Anisha. Visit her at the SAHS today! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill's Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd., visit SAhumane.org, or call (210) 226-7461.",
    })

def pet_14() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "WHISPER",
        "url": "id31697352",
        "text": "Age Senior Sex: F Size: M Breed: Cattle Dog Shelter: San Antonio Humane Society City: San Antonio If you are looking for a low-key girl to join you on daily walks and to explore the world with, Whisper is your girl. Her secret is that she is a 7 year old Australian Cattle Dog mix that longs for her forever home with adults. When you first meet her, you will notice that she is quite shy. She needs someone who will take the time to love her and show her that the world is not a scary place. While walking, you will notice her impeccable leash manners as she walks beside or behind you the whole time and does not pull at all. Whisper will loves treats and takes them very gently. So stop by the SAHS today to meet the lovely Whisper! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill's Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd., visit SAhumane.org, or call (210) 226-7461.",
    })

def pet_15() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "SUZIE",
        "url": "id31709429",
        "text": 'Age: Adult Sex: F Size: L Breed: Shepherd Shelter: San Antonio Humane Society City: San Antonio Sweet, eager, and a great walking buddy perfectly describe Suzie. She is a 2 year old Shepherd mix who cannot wait to meet her forever family. Suzie loves her walks and would love to go on daily walks with her best friends. She is still learning leash manners, but with some practice, shell do great in no time. Suzie is super smart and is learning how to sit on command. She loves to be loved on and will gladly give you kisses in return. If you are looking for a girl who will give you unlimited laughs and love, Suzie is your girl. She cannot wait to join her forever family! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd., visit SAhumane.org, or call (210) 226-7461.',
    })

def pet_16() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "KODIAK",
        "url": "id31715000",
        "text": 'Age: Adult Sex: F Size: M Breed: Siberian Husky Shelter: San Antonio Humane Society City: San Antonio Beautiful, sweet, and smart - those words describe Kodiak perfectly. She is a 7 year old Siberian Husky mix who is eagerly awaiting a new home with a caring and compassionate family. Kodiak would do best in a home with adults and older kids. She isnt a fan of felines and is interested in meeting your canine companion prior to being adopted. Kodiak has pretty brown eyes, a lovable face, and a mostly white fluffy coat that many love to run their fingers through. This intelligent gal knows: sit, down, watch me, and leave it. Were sure with some practice, Kodiak will master many more commands! She loves her walks and is still learning how to do well on a leash; however, she is very smart and wants to make her people happy. Kodiak also loves chasing the ball! She does not always bring it back, but she will let you take it out of her mouth so you can throw it again and again. When she is not chasing after the ball or enjoying her walks, she is eagerly waiting to be loved on. She loves to be petted and cuddled, and will shower you with unlimited kisses and may even jump into your lap for a hug! Kodiak is eager to join her forever home so she can shower you with as much love as you give her. Come to the SAHS and meet her today! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. *** Adoption fees for dogs include: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd. or call (210) 226-7461.',
    })

def pet_17() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "FROSTIE",
        "url": "id31732057",
        "text": 'Age: Young Sex: F Size: M Breed: Hound Shelter: San Antonio Humane Society City: San Antonio No snowman here, just Frostie, the pup in need of a caring family who will accept her shy demeanor. At first glance, you will notice her silky floppy ears, cute face, and soulful eyes. Frostie is a 1 year old Hound mix who is willing to show her true self once she feels comfy with her people. She enjoys daily walks and does very well on a leash. So if you are interested in joining her on a stroll, stop by the SAHS today and give this sweet gal a chance! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd., visit SAhumane.org, or call (210) 226-7461.',
    })

def pet_18() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "PETRA",
        "url": "id31741191",
        "text": 'Age: Young Sex: F Size: M Breed: Retriever Shelter: San Antonio Humane Society City: San Antonio Meet Petra! She is an energetic 1 year old Retriever mix looking for a forever home. This happy-go-lucky chick loves to be the center of attention and hopes you will make her day by coming by the SAHS to meet her. She gets along well with others like her and is working on perfecting the sit command. Maybe you can help her reach her goal! Stop by the SAHS and take Petra for a walk she just might surprise you with her amazing personality! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd. or call (210) 226-7461.',
    })

def pet_19() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "MARLOW",
        "url": "id31762643",
        "text": 'Age: Senior Sex: M Size: L Breed: Shelter: San Antonio Humane Society City: San Antonio This sweet Oldie But Goodie is a Retriever and Great Dane mix who is looking for a special understanding family to welcome him into their home. Marlow is calm, a good leash walker, and takes treats gently. While on his short daily walks he might experience some discomfort due to his arthritis and would love to snuggle on a comfy bed/couch, after returning. Marlow takes yummy vitamins and will need to continue to do so in his new home. Unfortunately, his eyesight isnt as well as it once was, but once he gets used to his new home, he should do very well with his new surroundings. Marlow would do best in a home with older kids and adults and he is all in for a long head and neck rub hes even likely to gently lay his head into your hands for this amazing experience! He is a large dog, 64 pounds, with long elegant legs, a short smooth black coat, and white eyebrows that give him a distinguished wise look. This 10 year old is Heartworm Positive, therefore, he cannot be too active but luckily he has a special Guardian Angel in his life that wants to make sure he finds a loving forever home. Come by soon and ask to meet the talkative Marlow! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. *** Adoption fees for dogs include: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd. or call (210) 226-7461.',
    })

def pet_20() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "PRESLEY",
        "url": "id31763675",
        "text": 'Age: Senior Sex: M Size: M Breed: Terrier Shelter: San Antonio Humane Society City: San Antonio When you look at Presley, you wont be able to resist his cute under bite, but there is much more to him than that. This 7 year old Terrier mix is ready to find his forever home with an amazing family that he can spoil. When you come to meet him, you will quickly notice what a happy boy Presley is, he never stops wagging his tail! He will be very eager to join you on daily walks and even though he gets pretty eager to explore at first, he will calm down and does pretty well on a leash. Presley is intelligent and already knows how to sit, speak, and responds to the watch me command from his people. One way to practice these skills with him is to offer him yummy treats. To show his excitement and appreciation for the treats, Presley might ask for it with a little bark and paw reach. While he is heartworm positive, after a few more treatments he will be heartworm free. If you want a boy who is full of love, happiness, and energy all rolled into a little package, Presley is the one for you. Stop by the SAHS today! Please remember to spay/neuter your pets to help ensure every dog and cat born has a home waiting for them. San Antonio Humane Society, Connecting Friends for Life. Adoption fees for Dogs: 25 pounds & under - $99 26 pounds & over - $65 *Adoption fees may vary This adoption fee includes: spay/neuter surgery, first set of vaccinations, microchip, de-wormer, flea and heartworm prevention, collar, tag, complimentary wellness exam within the first 5 days of adoption, 14 day complimentary follow up care at any VCA animal hospital, 30 days 24PetWatch Pet Insurance, and a starter bag of Hill\'s Science Diet pet food. For more information, visit the San Antonio Humane Society at 4804 Fredericksburg Rd., visit SAhumane.org, or call (210) 226-7461.',
    })

def pet_21() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Nutmeg",
        "url": "id30279155",
        "text": 'Age: Senior Sex: F Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Nutmeg is a sweet senior who has bounced from house to shelter to house to shelter through no fault of her own. Now with Basset Buddies, she\'s looking for the truly loyal family who will make her a forever member. Nutmeg is healthy, gets along well with people and other dogs, and loves to give big sloppy kisses. Please apply to adopt her today!',
    })

def pet_22() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Scout",
        "url": "id30579440",
        "text": 'Age: Young Sex: M Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.8-year-old Scout was adopted from Basset Buddies in 2009 and recently returned through no fault of his own. He\'s hoping good fortune will strike again and a loving family will scoop him up for the rest of his life. Scout is healthy, housetrained, and friendly. Scout is very sweet and the perfect pet for older children. Please open your heart and your home to this affectionate fella and apply to adopt Scout today!FOSTER UPDATE (5/29/15): He\'s a sweetheart and my constant companion around the house. Gets along very well with our 2 basset girls. Doesn\'t show any food aggression. Has never had any kind of accident in the house. He does startle pretty easy with sudden noises - prefers a quite calm environment. He will try to instigate some play with our other 2 from time ot time. Enjoys rides in the truck. Friendly with visitors, but will let you know if someone is outside the house.',
    })

def pet_23() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Milo",
        "url": "id31640056",
        "text": 'Age: Senior Sex: M Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Meet Milo, a charming older guy who would love nothing more than to spend his golden years with a loving forever family. Milo is 11 years old, but he still has a lot of pep to his step. He\'s energetic and wants lots of attention! Milo had a benign mass removed from his side and is currently rocking stitches, but he\'s healing well and is ready for adoption. Please apply to adopt Milo today!',
    })

def pet_24() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Sherman III",
        "url": "id32005622",
        "text": 'Age: Young Sex: M Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Sherman III is a sweet 7-year-old who can\'t wait for a forever home of his very own. He\'s happy, good-natured, and very cute. Sherman gets along with other dogs and loves people. He\'ll make a loving, loyal companion for years to come. If your family\'s looking for a buddy, please apply to adopt Sherman today!FOSTER UPDATE (5/1/15): He is doing great! He\'s eating well and really playing. He gets along great with my babies but wants to stay real close to me and wants to snuggle with me at night to sleep.',
    })

def pet_25() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Huntley",
        "url": "id32086980",
        "text": 'Age: Senior Sex: M Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Huntley is a handsome older guy who finally knows the comforts of a loving home and tender loving care. He gets along great with people, other dogs and even cats. All he asks for is space when he eats and belly rubs when he\'s done. Please show Huntley the golden years he so richly deserves and apply to adopt him today!',
    })

def pet_26() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Rufus",
        "url": "id32096680",
        "text": 'Age: Senior Sex: M Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Rufus is a friendly, happy boy who is around 10 years old -- but he\'s a very young 10! He likes to take lots of naps, and nothing makes him happier than curling up on the couch to watch TV with his favorite human pals. He\'s also always up for a long walk or a chance to play fetch. His hobbies include hanging out with other dogs, sniffing everything, and meeting new people. He\'d love to be your new bestie, so please apply to adopt him today!',
    })

def pet_27() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Albert",
        "url": "id32128713",
        "text": 'Age: Senior Sex: M Size: XL Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Albert is a big, handsome fella who deserves better than the life he\'s had. Despite the neglect he\'s endured, Albert is happy and playful. He gets along well with people of all ages, dogs, and even cats. He is sooo happy to get any type of attention and wags his tail excitedly when he\'s cuddled, stroked, or loved. Albert would love nothing more than a loving home with lots of TLC in his golden years. Please apply to adopt Albert today!',
    })

def pet_28() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Eva",
        "url": "id32128714",
        "text": 'Age: Young Sex: F Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Hola! I\'m Senorita Eva from the Texas Valley. I\'m a bilingual (really!), 3-year-old slim basset, weighing just 35 pounds. I\'m muy bonita! My foster family finds me delightfully entertaining, charming, and sweet as sugar. I use a doggie door, walk on leash, and generally behave myself. I\'m not a picky eater if you\'ve got chicken. I need lots of amor. What do you say: mi casa es su casa? Eva is currently undergoing heartworm treatment and will be available for adoption soon.',
    })

def pet_29() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Remy",
        "url": "id32174377",
        "text": 'Age: Senior Sex: M Size: M Breed: Basset Hound Shelter: Basset Buddies Rescue of Texas City: Houston You can fill out an adoption application online on our official website.Remy is a large, very quiet, old man seeking the loving, devoted family he\'s always wanted. Just look at that heart on his side! Remy is 10 years old, gets along with other dogs, and loves people, especially men. He wants to play and loves to cuddle. This poor guy was dumped at a local shelter and endured painful dental surgery. Now he\'s ready to bask carefree in his golden years like every basset should! Please show Remy that life begins at 10 and apply to adopt him today!',
    })

def pet_30() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Buster",
        "url": "id25426324",
        "text": 'Age: Adult Sex: M Size: M Breed: Shelter: Texas Collie Rescue, Inc. City: Houston Buster is a precious 40 lb. 3 year old collie mix. Buster is house trained, crate trained and walks well on a leash. He likes men, woman and children. Buster would thrive being the only dog and complete center of attention or enjoy having another dog around for comradery. He enjoys going for car rides so plan to take him along! Buster would love to have his very own family since he has never had his own family. He has a lot of love to give. Adoption applications and a complete listing of all our adoptables can be found on our website: www.texascollierescue.org.FOLLOW US ON FACEBOOK! GET THE LATEST ON NEW ARRIVALS!',
    })

def pet_31() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Annabelle",
        "url": "id28776587",
        "text": 'Age: Adult Sex: F Size: L Breed: Collie Shelter: Texas Collie Rescue, Inc. City: Houston Annabelle is a 5 yo, female, spayed, tri (ultra-soft black, purest white ruff and red-gold) pending registration Old Time Scotch Collie (OTSC). The OTSC is the predecessor of today\'s collie breeds that became obsolete with the disappearance of the American family farm. These collies were more stocky, and hardy than today\'s collie, bred for independent thinking and the stamina to herd, hunt, and protect the family farm. There are only a few hundred of these dogs left, see http://www.scotchcollie.org/). So how did Annabelle wind up in Texas Collie Rescue (TCR)?The OTSCs that have been discovered in the U.S. have come from old family ranches and farms. And Annabelle is the right age to have been turned in the San Antonio Humane Society as a pup at about the time when the Texas drought forced many San Antonio area farmers and ranchers to sell land and livestock, and part with the dogs they used to work farms and ranches that had been in operation for hundreds of years. But Annabelle can\'t remember living on a farm, or being taken to a shelter, or adopted. Or her owner mistaking her for an Australian Shepherd because of her coloring and docking her tail? Or getting lost? Or being stolen? That was just too long ago. And the poor dog could not say how she wound up in the back yard of a house in San Antonio in a high crime neighborhood, where someone put down an endless supply of cheap dog food that led to her becoming overweight. A high of just shy of 90 doggy pounds!It seems that Annabelle CAN remember being made to fight with other dogs, that caused the scars on her face and tongue. She is still collie-friendly and wags her stub of a tail lovingly at every dog she meets. She even wags at cats, who don\'t seem to want to share the love. But because of her fighting experiences, she will fight, and not back away if she is attacked by an aggressive dog.Annabelle must be with a family with a gentle dog friend, or no other dog at all. She should not visit a dog park where aggressive dogs might attack her. And she should not live in a home with very young children who might startle her by poking a stick in her eye when mom or dad aren\'t looking. And yes your little darling will do it even if you don\'t think she/he will, because young kids just don\'t know any better! And Annabelle also seems to remember being left alone in a yard until there was no more food to eat, and finally breaking down a gate to try to find water and food. She wandered for days through a neighborhood that you and I would be afraid to hang out in after dark before she was caught by a Good Samaritan Rescuer, who called Texas Collie Rescue. So now Annabelle keeps a close (almost-human-in-intelligence-and-perception) eye on, and stays where she can always see her Foster Mom to be sure she is never abandoned again. And she will be a loyal and devoted friend to/protector of her new owner(s) forever.Annabelle just had her teeth cleaned and one broken tooth extracted. So she has a bright new Pepsodent smile, gentle brown eyes, and gorgeous soft coat. Other than being overweight, she is completely healthy (HW negative). Annabelle is outrageously smart, and could learn anything a dog can be trained to do, as you are inclined (obedience, herding), or just be a beautifully mannered best friend and protector. She can sit, shake, lie down and loves to go on loose leash walks (you could build endurance and work off those pounds together!).She is ready to love her new person/family forever. Annabelle is a special collie in many ways, and you will know after seeing her pictures and reading her story that she is YOUR dog. To adopt her, contact Linda at http://www.texascollierescue.org/',
    })

def pet_32() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Skylar",
        "url": "id29587332",
        "text": 'Age: Adult Sex: F Size: L Breed: Collie Shelter: Texas Collie Rescue, Inc. City: Houston My name is Skylar and I\'m one lucky girl! Texas Collie Rescue took me in and pretty much saved me. I was in really sad shape when I left the shelter. My fur was so matted they had to shave me. The shelter thought I was a boy and they were calling me King, turns out I was a girl under all that hair. Things are so much better for me now and I am ready to go to my forever home. How about you? My fur has grown out and is in full blown collie glory! I\'m great on the leash and like going for walks. I\'m house-trained and crate-trained too. When I\'m tired I put myself to bed. I do enjoy my bed since I didn\'t have one for the longest time.! I think you need a sweet collie girl like me to give you lots of love and attention. There\'s an application at www.texascollierescue.org that you need to fill out so you can meet me. I can\'t wait to meet you!SkylarSkylar is as sweet as can be. The shape she was in was unspeakable when she came to us. There is a before picture of her which doesn\'t even begin to show the bad shape she was really in. The groomer said it was the worst case they had ever seen. She was shaved down and now has her full coat back. She is a beautiful girl. All she wants is to be loved and to be near someone. Her eyes are beautiful and very expressive. We think she is about 6 years old. Over time she has become arthritic due to prior injuries.. We do give her supplements for this. She is a low-key, quiet dog. She would do best in a family with no children. We would love for you to open your heart and your home to her.',
    })

def pet_33() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Connor",
        "url": "id30748466",
        "text": 'Age: Young Sex: M Size: L Breed: Collie Shelter: Texas Collie Rescue, Inc. City: Houston Somy name is Connor, a young Sable Merle collie boy of less than a year. Now, I\'m a rather large boy, but don\'t let that put you off. I am friendly, sweet as can be and love to play! Did I mention I\'m a talker? I\'ve always got something to say. I can lay on the floor with my pal Rico and we just have a great big talk fest while we\'re playing. Wouldn\'t you like to have a talking collie? Sure you would! So hurry up and go to www.texascollierescue.org and fill out an application. I won\'t last long. Connor the Talking Collie Connor is a beautiful dog. He carries the Merle gene and has one blue eye and one brown. Along with that and his coloring it makes him quite striking. He is young and loves to play. And he is quite vocal. He and his buddy Rico play and talk all of the time. You could not ask for a sweeter dog. He gets along with all dogs and humans alike and likes to be loved on. He is house-trained and crate-trained. According to his paperwork he has had formal obedience training. He would be a great addition to any family. Please fill out an application if you are interested in him. We would love for this great boy to find his forever home.',
    })

def pet_34() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Rolo",
        "url": "id31073850",
        "text": 'Age: Young Sex: M Size: M Breed: Shelter: Texas Collie Rescue, Inc. City: Houston My name is Rolo, yep, you heard right. Just like the candy. So this is the deal. I am a smooth collie mix. I was left out around Lake Livingston to fend for myself. But, luckily, the person that found me called Texas Collie & Sheltie Rescue and they took me in. I\'m an energetic boy of a little over a year. My favorite pastimes are playing and more playing with a little nap time thrown in. I like dogs and people. Haven\'t ever met a cat so I don\'t know about that. But, my forever home would really, REALLY need to have a playmate for me. Did I mention I like to play???? If I fit the bill for you just fill out an application at www.texascollierescue.org. I can\'t wait to meet you!RoloRolo is a good-looking boy. Beautiful eyes rimmed in black, freckles on his nose, and a nice white ruff. He gets along well with other dogs (not sure about cats since there are none here), likes to play, but really likes attention, and is a happy and energetic dog. He would definitely need a playmate in his new home. Or someone who was in to running and would take him along. He is house-trained, crate-trained, and leash trained. We would love to hear from you if you are interested in him.',
    })

def pet_35() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Boots",
        "url": "id31074596",
        "text": 'Age: Adult Sex: M Size: L Breed: Collie Shelter: Texas Collie Rescue, Inc. City: Houston 59 lbs of awesome collie is waiting right here to meet you. My name is Boots, a good-looking sable and white collie boy hoping to find a new family this year. I like cats, humans, toys, and a good bowl of food. And I\'m house-broken. I mean really, what more could you ask for??? With all these good qualities you really can\'t miss. It\'s time for you to go to www.texascollierescue.org and fill out an application so you can meet me. BootsBoots is a great dog and very well-behaved. He loves attention and would probably do well as an only dog. While he does like people, he would not do well around young children. Best guess on age is that he is about three years old. He is a happy, friendly boy that deserves to have a new home in 2015. Let us hear from you if you are interested in him.',
    })

def pet_36() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Marshall",
        "url": "id31312816",
        "text": 'Age: Young Sex: M Size: L Breed: Collie Shelter: Texas Collie Rescue, Inc. City: Houston Are you looking for a collie hunk? My name is Marshall and here I am! A sweet, affectionate collie boy of about 1-1/2 years old who is looking for a forever home that has a collie buddy to play with. My foster mom says I need a doggie buddy to show me the rules of the house. I love to cuddle up in bed with my foster parents and give them kisses and I will do the same with you just give me half a chance. And with all my other good qualities like being well-mannered, house-trained, crate-trained and leash trained you can\'t miss. I tend to be a little shy at first but once I get to know you I will be a faithful companion for life. I\'m a laid back kind of guy that just wants to be near my people. If you want to meet me go www.texascollierescue.org and fill out an application. Thank you, Marshall. I\'ll be waiting for you to come for me.Marshall is a quiet, gentle sable and white collie boy. He weighs about 60 lbs. His foster parents cannot say enough about him. He loves to run and play as a young dog should and definitely needs another collie as a playmate. He is a very devoted boy to his foster family and canine foster brother and sisters. They allow him to run loose in the house and he has never caused a problem. He is good with other dogs, but is still shy towards strangers. Marshall does not do well around young children, but would do well with the older ones. This is one sweet boy! Let us know if you are interested in him.',
    })

def pet_37() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Kermit",
        "url": "id31713248",
        "text": 'Age: Adult Sex: M Size: S Breed: Shetland Sheepdog Sheltie Shelter: Texas Collie Rescue, Inc. City: Houston I am Kermit. I love people; especially ones that give me massages, peanut butter, and let me snooze in the sun. I have a favorite spot, right behind my ears, that I like to get rubbed. When that happens, I make a funny sound, because it feels so good! I get along with the dogs and people I have met here, including respectful children of all ages. I love to spend my time jogging or wrestling with energetic dogs since I really like to have fun. I need a house full of soft beds, people who like snuggles, and yummy treats! Do you think you have that? If that is the case please fill out an application. I would love to be part of your family. ( P.S. I\'m not green!) But what I will say is you need to hop on over to www.texascollierescue.org and fill out an application to meet me.KermitKermit is one special little - approx. 20 lbs. Sheltie. And once you look at his picture you will fall in love with him. He is so cute. Look at him posing! It looks like he knows he was on camera.',
    })

def pet_38() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Lady Di & Prince Charles",
        "url": "id32101616",
        "text": 'Age: Adult Sex: F Size: L Breed: Collie Shelter: Texas Collie Rescue, Inc. City: Houston Royalty has come to Texas Collie Rescue. Our names are Lady Di and Prince Charles. But we like being called Lady and Charlie. Those other names are a bit stuffy for us. We are brother and sister and are about 3 to 4 years old. If you need some walking buddies or want someone to help out with your errands we will gladly go with you. We really enjoy a good car ride. Charlie, my brother is a laid back kind of guy and me, I\'m more outgoing and nosey, but I prefer curious. We get along with other dogs, kids, and even like cats. Now here\'s the thing. Our forever home needs to be the same one. So if you are looking for two great family pups look no further. And then you can say you are part of the royal family!! Before you can meet us you need to go to www.texascollierescue.org and fill out an application. Check us out. My picture is the first one and Charlie is the second one. The third one is Charlie being laid back.Lady and CharlieWhen Lady and Charlie came to us they were in pretty sad shape. They were an owner surrender from Dennison, Texas. Their coats were so badly matted they had to be shaved. When they grow out they will be beautiful dogs. Their foster mom says they are both very sweet and are cuddlers. So if you are looking for some cuddle bugs we have them. Lady has the tendency to jump on people and would probably not do well with small children. However, they do need to go to their forever home together. They are bonded and we don\'t split them up when they are. Let us hear from you if you are interested. We want these furry kids to have a good and loving home!',
    })

def pet_39() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Jake",
        "url": "id32171997",
        "text": 'Age: Young Sex: M Size: M Breed: Australian Cattle Dog (Blue Heeler) Shelter: Texas Collie Rescue, Inc. City: Houston I know, I know. You\'re wondering how an Australian Cattle Dog wound up at a Collie and Sheltie Rescue. So the story is I was running around Irving with a buddy of mine. We were picked up and placed in a shelter. Now you know shelters aren\'t necessarily a good thing for us pups. But, since the rescue was told Arnie was a collie mix and I was his friend they took us both in. Way lucky for me! I have a warm bed and some good food now. I\'m a young one they say since my teeth are pretty and white. I\'ll be honest I\'m going to be a work in progress since I haven\'t learned all my doggie manners. But, these guys here are teaching me the ropes. I\'m a playful friendly sort. It would be nice for my forever home to have some in-house playmates. If you would like to make my acquaintance go to www.texascollierescue.org and fill out an application. I\'m ready to go anytime. Jake the Cattle DogJake is one good-looking dog and extremely sweet. He loves to be loved on. We weren\'t sure what he was initially but after we did some research and found some pictures of cattle dogs we were pretty sure that\'s what he is. He has all the markings, the coloring, and facial features right down to the bushy tail they have. So this boy is an Australian Cattle Dog. Best guess on his age is about a year and a half to two. He\'s friendly and loves to play. As he said he hasn\'t learned all his doggie manners. But, he\'s a smart boy and will be a fast learner. If you want to meet Jake go to our website and fill out an application.',
    })

def pet_40() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Hazel",
        "url": "id28941103",
        "text": 'Age: Adult Sex: F Size: M Breed: Calico Shelter: Give Me Shelter Cat Rescue City: San Francisco Hello...I\'m the lovely 3 year old Hazel! I\'m a DLH Calico-Tortie. w/white mittens and ascot! I\'m a sweet Queen and I love the feather toy to play with!For more information or to apply for Hazel, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10007[id=10007;ts=1437498120;0000000000]',
    })

def pet_41() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Nibbler",
        "url": "id28941105",
        "text": 'Age: Adult Sex: M Size: L Breed: Tabby - Brown Shelter: Give Me Shelter Cat Rescue City: San Francisco Nibbler is a big, cheeky boy, only 2 years old, a rich brown tabby. He has settled into his foster situation and now we see his true personality shine. He follows the foster around, seeking all the attention he can get. He will throw himself on the ground and show you his fuzzy belly. Nibbler is not comfortable with being picked up but would love to soak up your love and attention and pets.....purr, purr, purr.....For more information or to apply for Nibbler, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10009[id=10009;ts=1437498120;0000000000]',
    })

def pet_42() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Minnie",
        "url": "id29026471",
        "text": 'Age: Adult Sex: F Size: S Breed: Tabby Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi, my name is Minnie and let\'s be honest, I\'m looking for a zen like home. "Aren\'t we all?" you think. But I know my PURRfect home is out there. We just haven\'t found each other yet. Let me tell you a little bit about me, I\'d REALLY love to have you all to myself. Having to share a home with these other cats is just dreadful. Ok, I can compromise a little and maybe you have a more serene kind of cat that goes along with my zen goal. You see I can have issues with stress, I mean, don\'t we all? Serene is where it\'s at for me.Some things I really enjoy - eating, mealtime, playtime, treat time, did I mention meal time? My goal for a forever home is a loving family and a serene zen environment. Could we be a forever match?Please note:- Minnie is a Special Needs cat- Minnie would do best as an only child- Indoor onlyFor more information or to apply for Minnie, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10020[id=10020;ts=1437498120;0000000000]',
    })

def pet_43() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Purr",
        "url": "id31256107",
        "text": 'Age: Adult Sex: F Size: S Breed: Shelter: Give Me Shelter Cat Rescue City: San Francisco Courtesy Listing - You can meet Purr at Kitty Charm School in Mill Valley.Purr is a 4 year old calico Kitty Charm School rescued from the Monterey SPCA in May 2014. Purr was surrendered because her owner\'s husband died and she lost her job and house. Purr was very scared at the SPCA. She quickly settled in at Kitty Charm School and over time warmed to her new human family. We think she\'d be a great fit in a quiet home, probably happiest without small children or other cats. She\'d love someone willing to give her a chance to fall in love with him or her. Loves chin scratches and full body pets. Has a goofy playful side when she doesn\'t think you are looking. She loves head and neck kisses!Please email meow@kittycharmschool.com to learn how to adopt Purr.For more information or to apply for Purr, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10075[id=10075;ts=1437498120;0000000000]',
    })

def pet_44() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Daphne",
        "url": "id31485280",
        "text": 'Age: Adult Sex: F Size: S Breed: Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi, my name is Daphne and I\'m a super social and lovable girl. Everyone that talks about me says I have the best PURRsonality. You\'ll just have to meet me and see for yourself. One really neat thing about me is that I have extra toes (polydactyl) on my front and back paws which makes me pretty unique. Are you ready to meet me yet?Please note:- Daphne is polydactyl- Indoor onlyFor more information or to apply for Daphne, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10088[id=10088;ts=1437498120;0000000000]',
    })

def pet_45() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Maverick",
        "url": "id31609333",
        "text": 'Age: Adult Sex: M Size: L Breed: Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi, my name is Maverick and I\'m a friendly fellow. I don\'t want to you to just fall for my good looks though, I\'m looking for a committed person to give me a forever home. I do have some dietary needs to help me maintain my health. The folks at Give Me Shelter are working out what the perfect balance is and getting me back into good health. You see, I was lost in San Francisco which wasn\'t exactly the best for me. But now I\'m getting great food, a warm bed and good lovin\'. Interested in making me part of your family?Please note:- Maverick is a Special Needs cat- Indoor onlyFor more information or to apply for Maverick, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10095[id=10095;ts=1437498120;0000000000]',
    })

def pet_46() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Emerald aka Emmy",
        "url": "id31610509",
        "text": 'Age: Young Sex: F Size: S Breed: Domestic Short Hair-black Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi, my name is Emerald, but folks call me Emmy for short. Don\'t be fooled by my photo, I\'m not grumpy just a little nervous. I haven\'t learned all of my "social skills" yet. I\'m working on that with my foster mom. Here\'s my deal, I was born with a bent leg and they are checking out if it\'s a hindrance to my ability to get around or not. Since I\'m working on learning to trust my human friends, it has been a discovery process about my leg and it isn\'t quite clear yet. One thing I\'d really LOVE in my forever home is a more outgoing kitty friend that I can learn from. I\'m pretty young, so I think you\'ll find if you\'re committed to my continued growth, I will be a wonderful forever kitty.For more information or to apply for Emerald aka Emmy, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10099[id=10099;ts=1437498120;0000000000]',
    })

def pet_47() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Mittens",
        "url": "id31860373",
        "text": 'Age: Senior Sex: F Size: M Breed: Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi, my name is Mittens! I\'m an expert muffin maker and a lovable lady. I would very much like to be your one and only Queen Bee! Could you give a girl a chance?Please note:- Indoor onlyFor more information or to apply for Mittens, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10113[id=10113;ts=1437498120;0000000000]',
    })

def pet_48() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Leila",
        "url": "id32077928",
        "text": 'Age: Senior Sex: F Size: L Breed: Domestic Short Hair-black and white Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi! I\'m Leila and the folks at Give Me Shelter call me #LovableLeila! Why you might wonder? Because I am a complete LOVE! I love to be around you, I love affection and I love to cuddle! I especially love kisses on my head! Would you like a bundle of LOVE in your life? Then you\'ll want to meet me and we can be forever friends! I get along very well with my foster mom\'s animal kids, cat and dogs included! I prefer a quiet home, maybe even with a mellow cat friend. I get along ok with dogs but would rather cuddle with my human and cat friends, or maybe a smaller calm dog. I\'ve been through a lot after my family of 9 years didn\'t want to keep me anymore since the new kitty bullied me. I was a little scared and shy at first. But thankfully, Give Me Shelter saved me, found me a loving and patient foster family and gave me another chance to find a new furever home. I can\'t wait to be your loyal Leila and love you bunches!Please note:- Leila is a Special Needs catFor more information or to apply for Leila, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10123[id=10123;ts=1437498120;0000000000]',
    })

def pet_49() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Sammy Sweet Cheeks",
        "url": "id32077929",
        "text": 'Age: Adult Sex: M Size: M Breed: Shelter: Give Me Shelter Cat Rescue City: San Francisco Hi! I\'m Sammy, they call me Sammy Sweet Cheeks becuase of my adorable chubby cheeks. I\'m a super lovable and playful fellow. I\'m happy as your solo kitty and also get along well with other cats. Concerned about me being FIV+? Here\'s some great reading material from Best Friends to free you of any worries. I can live a long healthy life and safely with other cats. I hope you\'ll give me a chance to be your forever furkid!Please note:- Sammy Sweet Cheeks has tested positive for FIV- Indoor onlyFor more information or to apply for Sammy Sweet Cheeks, please go to:http://www.givemesheltersf.org/adoption/cat.php?id=10122[id=10122;ts=1437498120;0000000000]',
    })

def pet_50() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Molly",
        "url": "id31621544",
        "text": 'Age: Young Sex: F Size: S Breed: Persian Shelter: Persian and Himalayan Cat Rescue City: San Francisco Molly - Spayed Female 3 y/o White PersianDear little Miss Blue Eyes only has eyes for you! And those eyes and the rest of that big-hearted gal are looking forward to a new, fun, forever home where she can spend the rest of her happy life with lots of play and snuggles. Do you have a cat-friendly dog? No problem! She\'s been there, done that and is ready to do it again. Really, Molly is a fun-loving, super sweet girl who would love to find her perfect home. For info, call Pat - 925-838-1838.',
    })

def pet_51() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Derek",
        "url": "id31712486",
        "text": 'Age: Young Sex: M Size: M Breed: Himalayan Shelter: Persian and Himalayan Cat Rescue City: San Francisco Derek - Neutered Male ~2 y/o Lynx Point Himalayan MixDerek is a 2 year old Lynx Point Himalayan Mix. He would do very well with another mellow cat.Call Pat for more information: 925-838-1838.All PHCR cats are located in foster homes in the San Francisco, California area. All adoptions must be made in person. We do not ship cats.',
    })

def pet_52() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Lady",
        "url": "id32593901",
        "text": 'Age: Young Sex: F Size: M Breed: Persian Shelter: Persian and Himalayan Cat Rescue City: San Francisco Lady - Spayed Female 4 y/o Red PersianDear little Lady needs you! A little bashful at first, she totally warms up when a kind person interacts with her. We\'re hoping Lady\'s hero will come along with a forever home for Lady, and put a smile on her pretty face, ASAP.Call Pat for more information: 925-838-1838.All PHCR cats are located in foster homes in the San Francisco, California area. All adoptions must be made in person. We do not ship cats.',
    })

def pet_53() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Lisa",
        "url": "id32593914",
        "text": 'Age: Young Sex: F Size: M Breed: Persian Shelter: Persian and Himalayan Cat Rescue City: San Francisco Lisa- Red Persian, Spayed Female, Four-Years-OldPrecious little Lisa is just the sweetest thing. And, those beautiful eyes! Now, we\'re hoping a wonderful person comes along to take care of her, and give her a fantastic forever home!Call Pat for more information: 925-838-1838.All PHCR cats are located in foster homes in the San Francisco, California area. All adoptions must be made in person. We do not ship cats.',
    })

def pet_54() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Ginger",
        "url": "id18775606",
        "text": 'Age: Adult Sex: F Size: M Breed: Shelter: Animal Helper City: New Orleans Video of Ginger: http://animoto.com/play/2WgJBnDMwjlHBPPSwNGJ1QWe saw Ginger right before Christmas 2010. She was a stray and had puppies under a raised house. The shelter was contacted. They caught Ginger and her puppies. We took Ginger and the puppies into our rescue. Ginger was so bad off we thought she would die and the puppies would live. Ginger had bad heartworms and so many intestinal parasites that food was backing up in her stomach. She was super skinny but any when she ate her stomach got huge. Unfortunately, we were unable to save her puppies, as they had herpes did not survive. Ginger was treated and is now heartworm negative. Ginger loves attention. Her favorite activity is to have her belly rubbed. She just flips right over and shows her belly. She loves to cuddle and give kisses. She doesn\'t even move when I clip her nails. Ginger is afraid of most dogs. She can be walked in the park around other dogs and has no issue becaue she\'s only focused on you. Ginger has been loose in the yard with different dogs over the years. If they are not on a leash you can see her eyes get big and she\'s afraid. She\'s never hurt one. Once Ginger and another dog got out of their crates at a foster home. Ginger got the worst end of the deal. The other dog had barely a scratch. She kisses the other dogs through the kennels. She\'s approximately 6 years old and 30 lbs. She is a tiny light brown brindle pit bull. Ginger is up to date on shots, flea prevention and heartworm prevention. She had a negative fecal. She had a good vet exam. She\'s also microchipped. We\'ve had Ginger 3.5 years now. She stays in a crate because the foster has other dogs. Ginger is no longer happy and she\'s crying. Ginger recently got HGE, a disease caused by stress. We were able to fix her condition but we know Ginger is no longer happy and needs a new forever home asap. She is miserable and we desperately want her to have the loving home she deserves. Ginger has had a hard life and she deserves better. She needs a home without any other animals. Ginger would be good with an active person or a couch potato. She loves children. Ginger\'s fee is $100. If you are interested in Ginger, please email animalhelperneworleans@gmail.com',
    })

def pet_55() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Honey",
        "url": "id27994554",
        "text": 'Age: Adult Sex: F Size: S Breed: Shelter: Animal Helper City: New Orleans Honey was part of a cruelty case in rural Alabama. The family moved and left 20 dogs to fend for themselves. Honey had recently had puppies. She was covered in ticks, fleas, and lice. She also had demodex mange. She went through heartworm treatment and was spayed. Honey is very shy around new places as she was feral. She\'s learning to be a dog. She snuggles with her foster mom. She plays with the other dogs and with toys. She goes outside. She hates a crate though. She has come a long way, and is improving daily. She will do well once settled in a home of her own. She is 25 lbs and around 3-5 years old.Her adoption fee is $100. If interested in Honey, email us at animalhelperneworleans@gmail.com',
    })

def pet_56() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Kermit",
        "url": "id28303128",
        "text": 'Age: Adult Sex: M Size: L Breed: Domestic Short Hair - orange and white Shelter: Animal Helper City: New Orleans Kermit is a ~5 year old male short hair orange tabby. He was treated for giardia when he first arrived from the streets, which is a parasite from drinking nasty water. He\'s felv/fiv/hw negative. He\'s up to date on shots. He\'s on revolution for flea prevention. He\'s such a awesome cat. He\'s good with dogs and other cats, although he will let anyone know if they have crossed a line with him. :) He enjoys pets and cuddles. He purrs a lot. Loves to get attention. We think he would be perfect for a child. He\'s very relaxed. His fee is $76. If you are interested in Kermit email animalhelperneworleans@gmail.com',
    })

def pet_57() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Thelma",
        "url": "id29790090",
        "text": 'Age: Adult Sex: F Size: S Breed: Shelter: Animal Helper City: New Orleans Thelma is a 5 year old adorable mutt. According to Yappy Happy\'s petfinder she was born at JoyceCharles\' house on November 7, 2009. She is very timid as a result of living in that environment. She didn\'t get the proper socialization she needed in her early years. She will never be a normal dog but is making progress. She will now let me pick up her. She walks around the house wagging her tail and it\'s always upright. She will walk around if the new people in the house are sitting on the couch. If they are standing up or go near her she barks. We\'re working on this. She\'s spayed and heartworm negative. She\'s up to date on shots, flea and heartworm prevention. We have no idea on her breed, just super cute. She barks at the cats if door is closed but doesn\'t do anything if she\'s loose around the kittens. I think she\'s just watched and learned by the others acting up. Thelma\'s mother is a chihuahua. Because Thelma came from a hoarding situation, she is not yet housebroken but we are working on that. If you are interested in Thelma, please email animalhelperneworleans@gmail.com.',
    })

def pet_58() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Daphy",
        "url": "id31625530",
        "text": 'Sex: F Size: L Breed: Labrador Retriever Shelter: Animal Helper City: New Orleans Daphy was hit by a car a few weeks ago. She luckily didn\'t have any breaks. She\'s full of life & looking for her second chance at a wonderful full life. Daphy is young maybe 1 1/2 years & just a mutt. She\'s currently 55 lbs but skinny. Guess she\'ll be 60 lbs. She\'s a little timid at first but doesn\'t take long to warm up and be your best friend. She\'d love a foster to introduce her to a lot of people and places to show her life will no longer be cruel. It won\'t take long to change her outlook on life. This will greatly increase her chances of adoption as large mutts are our hardest to adopt. I think she would be a great running partner. Maybe a volunteer would want to test drive her (I can\'t run)? She loves to run in the backyard and play fetch. Someone has taught her manners. She jumps around me excitedly but never touches me. She walks great on a leash but does pull so that needs corrected. She\'s a perfect passenger in the car. I personally think she should only be crated for a few years. She\'s scared at being left again plus she\'s young. She\'s only barked in the crate when she needs to potty. She only wants outside to potty and come immediately inside unless someone is with her. She\'s dog and cat friendly. She\'s heartworm negative. She\'s up to date on shots, flea and heartworm prevention. She had xrays and exams to ensure she\'s healthy. She had a negative fecal. She\'s got a few more weeks before she can be spayed as she came to us in heat. Please email us at animalhelperneworleans@gmail.com if you\'d like to foster, adopt, socialize or take her for a run. She\'s going to make someone an excellent pet. She\'s currently in New Orleans, LA.',
    })

def pet_59() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Joy",
        "url": "id31625861",
        "text": 'Age: Young Sex: F Size: S Breed: Poodle Shelter: Animal Helper City: New Orleans Joy the poodle is looking for her forever home! She is such a sweet, smart girl & very loving! She plays with the other dogs in her foster home, is a huge cuddle bug & likes to give kisses & be held. She loves doing dog puzzles or learning new things, as she is extremely smart! Joy is very athletic & can jump high as well as climb. She would be awesome with someone who wants to do agility, although that\'s not a necessity because she is just as happy laying in your lap. The down side to this is that she can easily jump over a baby gate with no problem. A double baby gate (so two high in the doorway) will stop her or she also does not mind going in her kennel. Joy never tries to escape, she just always wants to be by her humans. She loves to follow her foster mom around the house or yard, lay in her lap or be held. She will flourish in a home that enjoys training, will keep her mentally stimulated & loves to cuddle! Joy has some social anxiety issues that we have been working on. When new people come into her house, she is not always friendly. She has never been known to bite, however, will growl or jump up. Joy also likes to guard her owners in bed at night so if one gets up & comes back, she may guard the one still laying down. As long as Joy is put up when strangers come into the home & sleeps in her kennel at night, you\'ll never have a better pet! Once she warms up to someone, though, she is extremely loving. Joy does well on a leash & in a kennel. She is housebroken & will even go out in the rain to hurry up & potty & come back. She\'s spayed and microchipped. She\'s heartworm negative and had a negative fecal. She\'s up to date on shots, Comfortis and heartworm prevention. Contact Animal Helper Rescue Group (animalhelperneworleans@gmail.com) for adoption information. Her adoption fee is $150',
    })

def pet_60() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Lt. Dan",
        "url": "id32483999",
        "text": 'Age: Baby Sex: M Size: S Breed: Shelter: Animal Helper City: New Orleans Lt Dan was brought to a local kill shelter. Government shelters cannot handle cases like this so they reached out to Animal Helper to save his life. (Nothing negative just a fact as they have very limited resources & we\'re always thankful they ask for help). His rear leg had been de-gloved & broken. We amputated his leg at 5 weeks. Nothing slows this sweet boy down! He loves to play and cuddle. He\'s doing well with potty training and kennel training. He loves other dogs and dog friendly cats. He\'s roughly 10 weeks old and weighs a little over 12 pounds. He is probably a pit bull mix. Please contact animalhelperneworleans@gmail.com if you are interested in adopting this wonderful boy!',
    })

def pet_61() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Mama D",
        "url": "id32484012",
        "text": 'Age: Adult Sex: F Size: L Breed: Australian Cattle Dog (Blue Heeler) Shelter: Animal Helper City: New Orleans Meet Ma D! Mama D is a 65lb, ~8 year old Australian Cattle Dog (Blue Heeler). Mama D was left on the property that Animal Helper purchased. She loves attention and will nudge you with her head. She is very nosy. Ma D is house- and crate-trained and will go out in the yard easily. She knows how to walk on a leash/harness, too.She likes to chew on toys so watch your shoes! She will also "steal" items like shoes and other small things. She doesn\'t chew on these, just takes them back to her bed.Mama D does very well with other dogs although she will let them know to keep their space. She does not bark often. Ma D did well enough with the one car ride we took; she stood in the back and looked out.Mama D is a gentle giant. She would love to find a home with plenty of doggy beds and loving hugs and kisses.Ma D would benefit from a nice yard she can lay around in the shade; she\'s fine outside for hours obviously prefers to be indoors.',
    })

def pet_62() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Sergio",
        "url": "id32484019",
        "text": 'Age: Adult Sex: M Size: L Breed: Shelter: Animal Helper City: New Orleans Sergio is looking for a foster home immediately. Sergio was left on the property when animal helper bought the new location. The property will be demolished in the next few weeks. Sergio cannot be there during this time & has no where to go. Remember black dogs are very hard to place. Mutts are harder to place. Bigger mutts are harder to place. We also have a harder time placing males. All these combined makes his chances slim. Sergio is 40 lbs & ~4 years old. He\'s neutered. Sergio is heartworm positive but will be on medicine to prepare him for heartworm treatement. Sergio is up to date on shots, heartworm & flea prevention. He had a great exam. Sergio was very shy when we met him two years ago. He now requests attention from anyone that comes on the property. He even jumps in the car and he used to be terrified of it. He will give kisses. He loves to lay against you while getting attention. Sergio wants to start his new life away from his horrible past. Are you willing to help him? Email animalhelperneworleans@gmail.com We are located in New Orleans.',
    })

def pet_63() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Romeo",
        "url": "id32484029",
        "text": 'Age: Adult Sex: M Size: S Breed: Chihuahua Shelter: Animal Helper City: New Orleans Romeo the Chihuahua is looking for his forever home! He is a sweet, smart boy & very loving! Romeo was surrendered after his best friend (a young girl) was diagnosed with a terminal illness. Romeo loves children as a result. He gets so excited on his walks when he sees kids. Romeo is 2 years old. He plays with the other dogs in his foster home, and would love to play with the cats if they\'d allow it. He is a huge cuddle bug and loves to burrow under the covers in bed. His favorite activities are fetching his toys and learning new things, as he is extremely smart! Romeo is very athletic & can jump high. He loves to follow his foster mom around the house with toys and quickly sits for treats. He does not mind going in his kennel. He will flourish in a home that enjoys training, and will keep him mentally stimulated. Romeo has some social anxiety issues that we have been working on. He\'s currently on Prozac. When new people come into his house, he will growl or bark. He has never been known to bite and calms down after the new people sit and talk to him. After a few minutes of getting to know the new humans, he usually picks one and sits in their lap. Once he warms up to someone he is extremely loving and will invite them to play. Romeo gets very excited to go on walks and pulls a bit on a leash at first, but calms as soon as his nose takes over. He loves to smell new things on his walks. He is housebroken and will not go potty in his kennel. He is 7.5 lbs. He\'s neutered and microchipped. Romeo is also heartworm negative and had a negative fecal. He\'s up to date on shots, flea, and heartworm prevention. Email animalhelperneworleans@gmail.com for adoption information. Romeo joined us December 29, 2014.',
    })

def pet_64() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Cayenne",
        "url": "id24096040",
        "text": 'Age: Adult Sex: M Size: XL Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans This sweet kitten is all loves and kisses. What a sweetheart, waiting for the right person to come along and adopt him! His mother was found right before he was born. A wonderful rescuer took her home and allowed her to have her kittens. Now he is ready for his own forever home. Maybe that is you? To meet him, contact his foster mom at Nolasark44@gmail.com or through the web site. He is neutered and fully vaccinated...and waiting for the right person.This sweetheart just made 2 years this month. He is super sweet and his heart is as large as his body. He is easy-going and likes to play and rub around his owner\'s legs. He has never been outside so we recommend him to an indoor only home. If you\'d like to meet this big boy, contact us and we can set up a meet and greet!',
    })

def pet_65() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Thomas",
        "url": "id24127186",
        "text": 'Age: Adult Sex: M Size: L Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans This wonderful kitty is looking for a forever home. They were abandoned by previous owners and cannot understand why. They did nothing wrong but love and trust humans. This wonderful, sweet, loving cat is looking for a home to once again call their own. Everyone comes with a story. Everyone of these sweethearts will win your heart over. Make this wonderful rescue cat your own.Thomas is 3 years old and very friendly and playfulHe\'s not a lap cat but loves to play with toys dogs and other catsThomas is shy so he can go home for a foster to adoptContact us asap to meet this boy',
    })

def pet_66() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Kayle",
        "url": "id24145389",
        "text": 'Age: Adult Sex: F Size: M Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans Lovable shy lady who fostered two kittens in addition to her own. Typically quiet, but loves to be petted! My little Saints colored lion needs stable home! Any accountants or librarians around? She is most frequently found on the bed or greeting you at the door.Kalye is 1 and 1/2 years old, spay and ready for her forever home.',
    })

def pet_67() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "STAR",
        "url": "id24145418",
        "text": 'Age: Adult Sex: M Size: L Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans Slightly more affectionate than Sarge he wants to be a lap cat, this will be very interesting as they are both over 20 pounds. They play with just about anything but prefer to interact with people. Neither one seems to mind dogs and tolerate other cats well ready for his forever home...this sweet cat is a true lap cat.',
    })

def pet_68() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Angelina",
        "url": "id24145433",
        "text": 'Age: Adult Sex: F Size: M Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans A 7mnth old Bengal cross female .She is a little shy but loves the laser pointer. Really needs to stay with her brother Brad as they have never been apart. Crazy for Crispies treats.Angelina is spay, vaccinated and fully tested for all feline diseases...and ready for her new home!',
    })

def pet_69() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Brad",
        "url": "id24145440",
        "text": 'Age: Adult Sex: M Size: M Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans Unlike his sister he is a lot more self-assured and the perfect companion for his sister. Despite their fierce reputation these Bengal mixes are the most unassuming pair and are in need of a home where they can get lots of attention and reassurance to reach their full potential.',
    })

def pet_70() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Sampson",
        "url": "id24145456",
        "text": 'Age: Adult Sex: M Size: XL Breed: Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans He was found behind the local Sam\'s Club where someone dumped him. Wet and hungry all he wanted to do was be held. Now his is a 20 lb cuddlebug who has paws like a cougar. He definitely needs a place in your arms or next to you anytime you are home and lots of room to run and play.',
    })

def pet_71() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Moine (indoor outdoor)",
        "url": "id24160479",
        "text": 'Age: Adult Sex: F Size: M Breed: Tortoiseshell Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans Moine is a mother of 5 kittens and is extremely exotic in her look. She is the typical tortiseshell cat and likes to be petted, but also likes her alone time. Moine likes to sit next to her owner and purr non-stop, but she is not super cuddly. Moine was a lost cat and was taken in while pregnant. She had her kittens last year at this time, was spay and fully vaccinated and tested. Now she has no interest in going outside anymore. She tolerates dogs and cats, but kittens can get on her nerves. She has no trouble voicing her opinions.If you want to meet this exotic, sweet girl, contact her foster parents at nolasark44@gmail.com or through the web site.',
    })

def pet_72() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Valinda",
        "url": "id24202785",
        "text": 'Age: Adult Sex: F Size: XL Breed: Siamese Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans Meet Valinda, a wonderful but shy Lynx Point Siamese. She is super loving to all humans but a bit timid around agressive cats and dogs. She is used large dogs. Like many siamese she is opionated-cattitude-and loves to lay around. Her next favorite thing to do is to sit by the her owner and purr up a storm. She is not picky about food, but does not miss a meal. She would do best in a quiet environment with many to love her.Valinda has seasonal allergies easily treated with over-the-counter antihistamines.She is extra large in size and in heart!',
    })

def pet_73() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Sam Elliott",
        "url": "id24257781",
        "text": 'Age: Young Sex: M Size: L Breed: Tabby - Grey Shelter: Advocate & Rescue-Operation Save the Whodatt Fur Babies City: New Orleans This sweet kitten is all loves and kisses. What a sweetheart, waiting for the right person to come along and adopt him! His mother was found right before he was born. A wonderful rescuer took her home and allowed her to have her kittens. Now he is ready for his own forever home. Maybe that is you? To meet him, contact his foster mom at Nolasark44@gmail.com or through the web site. He is neutered, microchipped, and fully vaccinated...and waiting for the right person.Elliott (as we call him) is about 42 yo and about 12 pounds. He is available immediately.',
    })

def shelters() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Visit a shelter",
        "url": "shelters",
        "text": 'About Shelters: Looking to adopt? Visit or get in contact with a shelter in your area. Logo Name City State Phone E-mail shelters    Greyhound Pets of America/Central Texas Austin  TX  855-4Go-Fast    placement@gpa-centex.org shelters    Small Chance Rescue Austin  TX  512-699-7244    info@smallchancerescue.com shelters    Humming for a Loving Forever Home   San Antonio TX  email   HummingforaLovingForeverHome@aol.com shelters    San Antonio Humane Society  San Antonio TX  210-226-7461    adoption@sahumane.org shelters    Basset Buddies Rescue of Texas  Houston TX  (281)-657-7347  info@bbrtx.org Texas Collie Rescue, Inc.   Houston TX  713-545-7408    info@texascollierescue.org shelters    Give Me Shelter Cat Rescue  San Francisco   CA  415-810-7284    info@givemesheltersf.org shelters    Persian and Himalayan Cat Rescue    San Francisco   CA  (925) 838-1838  info@persiancats.org shelters    Animal Helper   New Orleans LA      AnimalHelperNewOrleans@gmail.com Advocate & Rescue-Operation Save the Whodatt Fur Babies New Orleans LA  504-430-6730    hcalmes@yahoo.com',
    })

def shelter_1() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Greyhound Pets of America/Central Texas",
        "url": "TX192",
        "text": 'P.O. BOX 10069 Austin, TX 855-4Go-Fast placement@gpa-centex.org TX192 I love these people. My greyhounds love them, too, since they found their way to their forever home through them. These folks are fantastic to work with if...',
    })

def shelter_2() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Small Chance Rescue",
        "url": "TX1148",
        "text": 'P.O. Box 10033 Austin, TX 512-699-7244 info@smallchancerescue.com TX1148 Love, love, love this place! I have so much respect for the people who work & volunteer here. They are all doing it for the right reasons, the animals.',
    })

def shelter_3() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Humming for a Loving Forever Home",
        "url": "TX1680",
        "text": '1111 not available San Antonio, TX email HummingforaLovingForeverHome@aol.com TX1680 Outstanding. Everything is made fresh. Blue cheese dressing is delicious. All steaks and chops are hand cut. The standout is jumbo shrimp. Hands down the...',
    })

def shelter_4() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "San Antonio Humane Society",
        "url": "TX295",
        "text": '4804 Fredericksburg Road San Antonio, TX 210-226-7461 adoption@sahumane.org TX295 This is the most clean well kept animal shelter I\'ve ever perused. And even though I\'m biased because my pup adopted me here, I can say with confidence that...',
    })

def shelter_5() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Basset Buddies Rescue of Texas",
        "url": "TX1051",
        "text": 'P.O. Box 130244 Houston, TX (281)-657-7347 info@bbrtx.org TX1051 My fiance and I were thinking about adopting a pet so I looked into friends for life. One day we decided to visit and we were impressed by their facility...',
    })

def shelter_6() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Texas Collie Rescue, Inc.",
        "url": "TX1283",
        "text": 'Houston, TX 713-545-7408 info@texascollierescue.org TX1283',
    })

def shelter_7() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Give Me Shelter Cat Rescue",
        "url": "CA1061",
        "text": 'PO Box 411013 San Francisco, CA 415-810-7284 info@givemesheltersf.org CA1061 I am absolutely amazed by the people who run this organization. Of course, such rescue organizations are run purely by volunteers, but I think that this...',
    })

def shelter_8() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Persian and Himalayan Cat Rescue",
        "url": "CA1063",
        "text": 'Foster homes in the San Francisco Bay area San Francisco, CA (925) 838-1838 info@persiancats.org CA1063 4 of my mom\'s 6 cats came from here. They are amazing. (the other 2 she won in a carnival and she doesn\'t like them as much)',
    })

def shelter_9() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Animal Helper",
        "url": "LA204",
        "text": 'New Orleans, LA AnimalHelperNewOrleans@gmail.com LA204 Disclaimer: I have only eaten here drunk but I\'m pretty sure this place is good no matter what. Both times I was wearing white (once during white linen...',
    })

def shelter_10() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "Advocate & Rescue-Operation Save the Whodatt Fur Babies",
        "url": "LA305",
        "text": 'New Orleans, LA 504-430-6730 hcalmes@yahoo.com LA305',
    })

def cities() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='cities', body={
        'title': 'Cities',
        'url': 'cities',
        'text': 'New to the area? Traveling to a nearby city to find that purrfect pal? Or just looking for something fun to do? Find the top rated vet, groomer, and dog park in the area. Austin TX  US  cities Austin vet  cities Austin park cities Austin groomer city    San Antonio TX  US  cities San Antonio vet cities San Antonio park    cities San Antonio groomer city    Houston TX  US  cities Houston vet cities Houston park    cities Houston groomer city    San Francisco   CA  US  cities San Francisco vet   cities San Francisco park  cities San Francisco groomer city    New Orleans LA  US  cities New Orleans vet cities New Orleans park    cities New Orleans groomer',
    })

def city_1() :

    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Austin',
        'url': 'austin',
        'text': 'TX  US  Bat City, The City of the Violet Crown, The Live Music Capital of the World, The Blueberry in a Red State. These are some of the names that characterize Shelters in Austin Pets in Austin Vets in Austin',
    })

def city_2() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'San Antonio',
        'url': 'san_antonio',
        'text': 'TX  US I could put on my teacher\'s glasses and give you a history lesson on San Antonio. I could put on some tennis shoes and transform into a tour guide through Shelters in San Antonio Pets in San Antonio Vets in San Antonio',
    })

def city_3() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'Houston',
        'url': 'houston',
        'text': 'TX  US LOL.  The only thing I don\'t like about this city is the damn rain!  So many memories.  -Being Miss Upward Bound at Texas Southern University.  What up Shelters in Houston Pets in Houston Vets in Houston',
    })

def city_4() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'San Francisco',
        'url': 'san_francisco',
        'text': 'CA  US Sang to the tune of the \"Twelve Days of Christmas \") Fivvvvve parking tickets ....4 rainbow flags....., 3 Union Squares......., 2 Uber rides........ Shelters in San Francisco Pets in San Francisco Vets in San Francisco ',
    })

def city_5() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        'title': 'New Orleans',
        'url': 'new_orleans',
        'text': 'LA  US Had an excellent time here in New Orleans or NOLA as a lot of people say! We ate so much wonderful food. I feel like I was always full. Never hungry',
    })

def extapi() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "External API",
        "url": "extapi",
        "text": 'Adopt your favorite Dota 2 hero\'s companion, and embark on adventures of your own. Learn more about Dota 2 at Hat Fancy. Hero Main Item Main Set Hero\'s Companion Abaddon Cloak Of The Resentful Spectre  Darkness Wanderers Armor Set    Boots Alchemist   Assistant\'S Blades Of Scientific Inquiry    Alchemy Essentials Set  Angelina Anti-Mage   Adornment Of The Clergy Ascetic The Clergy Ascetic Set  Daphne Axe Axe Of The Red Conqueror    The Red Conqueror Set   Rufus Batrider    Bertha The Morde-Bat    The Rough Rider Of Yama Raskav Set  Cayenne Beastmaster Ancestral Axes Of Karroch   Custom Of Karroch Set   Buster Bloodseeker Belt Of The Blood Covenant  Wrath Of The Blood Covenant Set Nutmeg Bounty Hunter   Armor Of Distant Sands  Hunter In Distant Sands Set Lisa Brewmaster  Battlejug Of The The Drunken Warlord    The Drunken Warlord Set Lisa Bristleback Emerald Frenzy Amulet   Emerald Frenzy Set  SUZIE Broodmother Abdomen Of Perception   Webs Of Perception Set  Thomas Centaur Warrunner   Armguard Of The Steppe  Warrior Of The Steppe Set   Hazel Chaos Knight    Ataxia  Embers Of Endless Havoc Set Joy Chen    Armguards Of The Penitent Nomad Arms Of The Penitent Nomad Set  Sergio Clinkz  Bow Of The Crypt Guardian   Crypt Guardians Set Honey Crystal Maiden  Arctic Bracers Of The North Heart Of The North Set  Sam Elliott Dark Seer   Aqwanderer Boots    Aqwanderer Set  STAR Dazzle  Ancestral Arm Wrap  Ancestral Trappings Set Skylar Death Prophet   Armor From The Gloom    Gifts From The Gloom Set    Sampson Disruptor   Aegis Of The Storm  Rider Of The Storm Set  VINCE Dragon Knight   Armor Of The Drake  Fireblessed Mail Of The Drake Set   Ginger Drow Ranger Bow Of The Shadowcat    Gifts Of The Shadowcat Set  Hazel Earth Spirit    Mane Of The Demon Stone Strength Of The Demon Stone Set Kermit Earthshaker Belt Of The Forest Hermit   Forest Hermit Set   Kayle Ember Spirit    Arm Guards Of Prosperity    Flames Of Prosperity Set    Connor Enchantress Araceae\'S Tribute Bracelets Araceaes Tribute Set    Trixie Bell Faceless Void   Armor Of The Tentacular Timelord    The Tentacular Timelord Set Nutmeg Gyrocopter  Emerging Dragon Armaments Of The Dragon Emperor Set Romeo Huskar  Obsidian Blade Bracers  The Obsidian Blade Set  ANISHA Invoker Arcane Drapings Mnemonus Arcanus Set    Lady Di & Prince Charles Juggernaut  Akakiryu Of A Thousand Faces    Thousand Faces Set  Lady Di & Prince Charles Keeper Of The Light Bardings Of The First Light Dressings Of The First Light Set    Ginger Kunkka  Admiral\'S Foraged Cap   Armaments Of Leviathan Set  Turner Legion Commander    Armlet Of The Dragon Guard  Commander Of The Dragon Guard Set   Milo Leshrac Armor Of Twisted Wisdom Twisted Wisdom Set  Sherman III Lich    Bindings Of Eldritch Ice    Eldritch Ice Set    Mama D Lina    Adornments Of The Ember Crane   Ember Crane Set Albert Lion    Carapace Of Buki\'Vak The Corrupted  Curse Of The Malignant Corruption Set   Mama D Lone Druid  Braces Of The Atniw The Atniws Fury Set Sammy Sweet Cheeks Luna    Armor Of Eternal Eclipse    Blessings Of The Eternal Eclipse Set    Lillipup Lycan   Battle Claws Of The Great Grey  Form Of The Great Grey Set  Milo Medusa  Blouse Of Forsaken Beauty   Forsaken Beauty Set WHISPER Meepo   Bandana Of The Bone Ruin Bandits    Spoils Of The Bone Ruins Set    ANISHA Mirana  Andalmere The Litigon   The Moon Rider Set  Honey Morphling   Ancient Armor Arms  Ancient Armor Set   Joy Naga Siren  Armor Of The Slithereen Exile   The Slithereen Exile Set    Nibbler Nyx Assassin    Blades Of The Predator  Alpha Predator Set  Jake Ogre Magi   Belt Of Ancestral Luck  Ancestral Luck Set  Brad Omniknight  Armlet Of Renewed Faith Armor Of Renewed Faith Set  KODIAK Phantom Assassin    Belt Of The Gleaming Seal   Dread Of The Gleaming Seal Set  Skeeter Phantom Lancer  Ancestors\' Belt Ancestors Pride Set Lady Di & Prince Charles Pudge   Armor Of The Black Bird Murder Of Crows Maverick Pugna   Nether Grandmaster\'S Bite   The Nether Grandmasters Robes Set   Sam Elliott Queen Of Pain   Chain Of Enduring Torment   Bindings Of Enduring Torment Set    Scout Razor   Armor Of The Twisted Arc    The Twisted Arc Set Milo Riki    Blade Of The Subtle Demon   The Subtle Demon Set    FERLIN Rubick  Cloak Of Inscrutable Zeal   The Inscrutable Zeal Set    Vivian - Courtesy ListingSand King   Caustic Glare   The Caustic Consumption Set Albert Shadow Demon    Bindings Of The Summoned Lord   Chains Of The Summoned Lord Set Marshall Shadow Shaman   Eki Bukaw Bracers   Eki Spiritual Implements Set    STAR Silencer    Arms Of The Silent Champion Silent Champion Mittens Skywrath Mage   Belt Of Retribution The Arms Of Retribution Set Thelma Slardar Deep Vault Guardian Armplates   Arms Of The Deep Vault Guardian Set Sampson Slark   Deep Warden\'S Conch Pauldron    Deep Warden Haul Set    Sampson Sniper  Bracers Of The Howling Wolf Spirit Of The Howling Wolf Set  Daphy Spectre Belt Of The Eternal Light   The Eternal Light Set   Amigo Spirit Breaker  Battleseeker Arms   Battleseeker Set    FERLIN Storm Spirit    Festive Robes Of Good Fortune   Gifts Of Fortune Set    Valinda Sven    Armblade Of The Chiseled Guard  Raiment Of The Chiseled Guard   Ginger Templar Assassin    Brooch Of The Third Insight The Third Insight Set   MARLOW Tidehunter  Cerebral Support    The Paleogeneous Punisher Set   Sam Elliott Tusk    Arctic Hunter\'S Glove   Arctic Hunter Set   Hazel Ursa    Armor Of A Savage Age   The Savage Age Set  Jake Warlock Bracers Of The Archivist    The Demonic Archivist Set   PRESLEY Weaver  Antennae Of The Master Weaver   Master Weaver Set   Mittens Windranger  Arc Of The Northern Wind    The Northern Wind Set   STAR Witch Doctor    Beak Of The Stormcrow   The Stormcrows Spirit Set   Skeeter Wraith King Arms Of Eternal Reign   Armor Of Eternal Reign  Huntley',
    })

def about() :
    es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
    es.index(index='gtp_index', doc_type='city', body={
        "title": "About Us N.S.A.I.D!",
        "url": "about",
        "text": 'Our aim is to provide easy access to information about animal shelters and other pet related services. We target anyone interested on adopting or keeping up with their pet\'s care. Sam Morris Group Leader for Phase 1 Bio: Like the rest of the team, Sam is a rank amateur when it comes to web development and hasn\'t slept in a week. Major Responsibilities: Project management, data collection, Apiary api documentation, tech report No. of Commits: 58 No. of Issues: 13 No. of Unit Tests: 8 Alexander Adams  Group Leader for Phase 2 Bio: Alex is a CS student, has long hair, and is our de facto django expert. Major Responsibilities: VM management, DNS, django installation and management, tech report No. of Commits: 44 No. of Issues: 5 No. of Unit Tests: 8 Nelma Perera Bio: Nelma is a major night owl. Major Responsibilities: Travis setup, dependency untangling, unit testing, django, UML data modeling No. of Commits: 145 No. of Issues: 6 No. of Unit Tests: 8 Ian Smith Bio: Ian is a CS student, used to have long hair, and is one of our two on the Frontend team. Major Responsibilities: Bootstrap, angular, html No. of Commits: 94 No. of Issues: 9 No. of Unit Tests: 8 Daniela Reyes Bio: Daniela, hailing from El Paso, is another of our de facto angular and html experts on the Frontend team. Major Responsibilities: Bootstrap, angular, html, tech report No. of Commits: 98 No. of Issues: 11 No. of Unit Tests: 7 Stats: Total no. of commits: 439 Total no. of issues: 51 Total no. of unit tests: 39 Data Data Sources: https://www.petfinder.com/developers/api-docs Scraping Method: https://github.com/nsaid-team/gotopaws/wiki/All-Things-API Apiary API Github Issue Tracker Github Repo Github Wiki Unit Test',
    })


if __name__ == "__main__" :

    home()

    pets()

    pet_1()
    pet_2()
    pet_3()
    pet_4()
    pet_5()
    pet_6()
    pet_7()
    pet_8()
    pet_9()
    pet_10()
    pet_11()
    pet_12()
    pet_13()
    pet_14()
    pet_15()
    pet_16()
    pet_17()
    pet_18()
    pet_19()
    pet_20()
    pet_21()
    pet_22()
    pet_23()
    pet_24()
    pet_25()
    pet_26()
    pet_27()
    pet_28()
    pet_29()
    pet_30()
    pet_31()
    pet_30()
    pet_32()
    pet_33()
    pet_34()
    pet_35()
    pet_36()
    pet_37()
    pet_38()
    pet_39()
    pet_40()
    pet_41()
    pet_42()
    pet_43()
    pet_44()
    pet_45()
    pet_46()
    pet_47()
    pet_48()
    pet_49()
    pet_50()
    pet_51()
    pet_52()
    pet_53()
    pet_54()
    pet_55()
    pet_56()
    pet_57()
    pet_58()
    pet_59()
    pet_60()
    pet_61()
    pet_62()
    pet_63()
    pet_64()
    pet_65()
    pet_66()
    pet_67()
    pet_68()
    pet_69()
    pet_70()
    pet_71()
    pet_72()
    pet_73()
    
    shelters()

    shelter_1()
    shelter_2()
    shelter_3()
    shelter_4()
    shelter_5()
    shelter_6()
    shelter_7()
    shelter_8()
    shelter_9()
    shelter_10()

    cities()

    city_1()
    city_2()
    city_3()
    city_4()
    city_5()

    extapi()

    about()