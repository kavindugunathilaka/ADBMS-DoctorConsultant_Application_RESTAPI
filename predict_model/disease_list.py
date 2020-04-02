DISEASE_LIST = [
        "Heberden's node", "Murphy's sign", "Stahli's line", 'abdomen acute', 'abdominal bloating', 'abdominal tenderness', 'abnormal sensation', 'abnormally hard consistency',
        'abortion', 'abscess bacterial', 'absences finding', 'achalasia', 'ache', 'adverse effect', 'adverse reaction', 'agitation',
        'air fluid level', 'alcohol binge episode', 'alcoholic withdrawal symptoms', 'ambidexterity', 'angina pectoris', 'anorexia', 
        'anosmia', 'aphagia', 'apyrexial', 'arthralgia', 'ascites', 'asterixis', 'asthenia', 'asymptomatic', 'ataxia', 'atypia', 'aura', 
        'awakening early', 'barking cough', 'bedridden', 'behavior hyperactive', 'behavior showing increased motor activity', 'blackout', 
        'blanch', 'bleeding of vagina', 'bowel sounds decreased', 'bradycardia', 'bradykinesia', 'breakthrough pain', 'breath sounds decreased', 
        'breath-holding spell', 'breech presentation', 'bruit', 'burning sensation', 'cachexia', 'cardiomegaly', 'cardiovascular event', 'cardiovascular finding',
        'catatonia', 'catching breath', 'charleyhorse', 'chest discomfort', 'chest tightness', 'chill', 'choke', 'cicatrisation', 'clammy skin', 'claudication', 
        'clonus', 'clumsiness', 'colic abdominal', 'consciousness clear', 'constipation', 'coordination abnormal', 'cough', 'cushingoid facies', 'cushingoid\xa0habitus', 
        'cyanosis', 'cystic lesion', 'debilitation', 'decompensation', 'decreased body weight', 'decreased stool caliber', 'decreased translucency', 'diarrhea', 'difficulty',
        'difficulty passing urine', 'disequilibrium', 'distended abdomen', 'distress respiratory', 'disturbed family', 'dizziness', 'dizzy spells', 'drool', 'drowsiness', 
        'dullness', 'dysarthria', 'dysdiadochokinesia', 'dysesthesia', 'dyspareunia', 'dyspnea', 'dyspnea on exertion', 'dysuria', 'ecchymosis', 'egophony', 'elation', 
        'emphysematous change', 'energy increased', 'enuresis', 'erythema', 'estrogen use', 'excruciating pain', 'exhaustion', 'extrapyramidal sign', 'extreme exhaustion', 
        'facial paresis', 'fall', 'fatigability', 'fatigue', 'fear of falling', 'fecaluria', 'feces in rectum', 'feeling hopeless', 'feeling strange', 'feeling suicidal', 
        'feels hot/feverish', 'fever', 'flare', 'flatulence', 'floppy', 'flushing', 'focal seizures', 'food intolerance', 'formication', 'frail', 'fremitus', 'frothy sputum', 
        'gag', 'gasping for breath', 'general discomfort', 'general unsteadiness', 'giddy mood', 'gravida 0', 'gravida 10', 'green sputum', 'groggy', 'guaiac positive', 'gurgle',
        'hacking cough', 'haemoptysis', 'haemorrhage', 'hallucinations auditory', 'hallucinations visual', 'has religious belief', 'headache', 'heartburn', 'heavy feeling',
        'heavy legs', 'hematochezia', 'hematocrit decreased', 'hematuria', 'heme positive', 'hemianopsia homonymous', 'hemiplegia', 'hemodynamically stable', 'hepatomegaly', 
        'hepatosplenomegaly', 'hirsutism', 'history of - blackout', 'hoard', 'hoarseness', 'homelessness', 'homicidal thoughts', 'hot flush', 'hunger', 'hydropneumothorax', 
        'hyperacusis', 'hypercapnia', 'hyperemesis', 'hyperhidrosis disorder', 'hyperkalemia', 'hypersomnia', 'hypersomnolence', 'hypertonicity', 'hyperventilation', 'hypesthesia', 
        'hypoalbuminemia', 'hypocalcemia result', 'hypokalemia', 'hypokinesia', 'hypometabolism', 'hyponatremia', 'hypoproteinemia', 'hypotension', 'hypothermia, natural', 
        'hypotonic', 'hypoxemia', 'immobile', 'impaired cognition', 'inappropriate affect', 'incoherent', 'indifferent mood', 'intermenstrual heavy bleeding', 'intoxication', 
        'irritable mood', 'jugular venous distention', 'labored breathing', 'lameness', 'large-for-dates fetus', 'left\xa0atrial\xa0hypertrophy', 'lesion', 'lethargy', 
        'lightheadedness', 'lip smacking', 'loose associations', 'low back pain', 'lung nodule', 'macerated skin', 'macule', 'malaise', 'mass in breast', 
        'mass of body structure', 'mediastinal shift', 'mental status changes', 'metastatic lesion', 'milky', 'moan', 'monoclonal', 'monocytosis', 'mood depressed',
        'moody', 'motor retardation', 'muscle hypotonia', 'muscle twitch', 'myalgia', 'mydriasis', 'myoclonus', 'nasal discharge present', 'nasal flaring', 'nausea', 
        'nausea and vomiting', 'neck stiffness', 'neologism', 'nervousness', 'night sweat', 'nightmare', 'no known drug allergies', 'no status change', 'noisy respiration',
        'non-productive cough', 'nonsmoker', 'numbness', 'numbness of hand', 'oliguria', 'orthopnea', 'orthostasis', 'out of breath', 'overweight', 'pain', 'pain abdominal', 
        'pain back', 'pain chest', 'pain foot', 'pain in lower limb', 'pain neck', 'painful swallowing', 'pallor', 'palpitation', 'panic', 'pansystolic murmur', 'para 1', 
        'para 2', 'paralyse', 'paraparesis', 'paresis', 'paresthesia', 'passed stones', 'patient non compliance', 'pericardial friction rub', 'phonophobia', 'photophobia', 
        'photopsia', 'pin-point pupils', 'pleuritic pain', 'pneumatouria', 'polydypsia', 'polymyalgia', 'polyuria', 'poor dentition', 'poor feeding', 'posterior\xa0rhinorrhea', 
        'posturing', 'presence of q wave', 'pressure chest', 'previous pregnancies 2', 'primigravida', 'prodrome', 'productive cough', 'projectile vomiting', 
        'prostate tender', 'prostatism', 'proteinemia', 'pruritus', 'pulse absent', 'pulsus\xa0paradoxus', 'pustule', 'qt interval prolonged', 
        'r wave feature', 'rale', 'rambling speech', 'rapid shallow breathing', 'red blotches', 'redness', 'regurgitates after swallowing', 'renal angle tenderness', 
        'rest pain', 'retch', 'retropulsion', 'rhd positive', 'rhonchus', 'rigor - temperature-associated observation', 'rolling of eyes', 'room spinning', 'satiety early', 
        'scar tissue', 'sciatica', 'scleral\xa0icterus', 'scratch marks', 'sedentary', 'seizure', 'sensory discomfort', 'shooting pain', 'shortness of breath', 'side pain', 
        'sinus rhythm', 'sleeplessness', 'sleepy', 'slowing of urinary stream', 'sneeze', 'sniffle', 'snore', 'snuffle', 'soft tissue swelling', 'sore to touch', 'spasm', 
        'speech slurred', 'splenomegaly', 'spontaneous rupture of membranes', 'sputum purulent', 'st segment depression', 'st segment elevation', 'stiffness', 'stinging sensation', 
        'stool color yellow', 'stridor', 'stuffy nose', 'stupor', 'suicidal',
        'superimposition', 'sweat', 'sweating increased', 'swelling', 'symptom aggravating factors', 'syncope', 'systolic ejection murmur', 'systolic murmur', 
        't wave inverted', 'tachypnea', 'tenesmus', 'terrify', 'thicken', 'throat sore', 'throbbing sensation quality', 'tinnitus', 'tired', 'titubation', 'todd paralysis', 
        'tonic seizures', 'transaminitis', 'transsexual', 'tremor', 'tremor resting', 'tumor cell invasion', 'unable to concentrate', 'unconscious state', 'uncoordination', 'underweight', 
        'unhappy', 'unresponsiveness', 'unsteady gait', 'unwell', 'urge incontinence', 'urgency of\xa0micturition', 'urinary hesitation', 'urinoma', 
        'verbal auditory hallucinations', 'verbally abusive behavior', 'vertigo', 'vision blurred', 'vomiting', 'weepiness', 'weight gain', 'welt', 'wheelchair bound', 'wheezing', 
        'withdraw', 'worry', 'yellow sputum']