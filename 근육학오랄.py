import random

def q3():
    z = [[
            ["external intercostal"], [
            "subcostalis",
            "posterior superior serratus",
            "pectoralis",
            "ant, mid, post scalene",
            "diaphragm"
        ]], [
            ["internal intercostal",
            "innermost intercostal"], [
            "transverse thoracic",
            "posterior inferior serratus",
            "rectus abdominis",
            "oblique abdominis",
            "quadratus lumborum"
    ]]]
    for i in range(2):
        print(["inspitation", "expiration"][i])
        for j in range(2):
            print(["agonist", "synergist"][j])
            input()
            print(z[i][j])
            print()
            
def q4():
    k = [
        "rectus abdominis",
        "linea alba",
        "tendinosus intersection",
        "rectus sheath",
        "linea semilunaris",
        
        "oblique abdominis",
        "external, internal, transverse oblique"
    ]
    
    print("6(9) keywords")
    input()
    for i in k:print(i)

def q6():
    d = {
        "clavicle": {
            "elevation": ["trapezius", "scm"],
            "depression": ["subclavius", "pectoralis major"]
        },
        "scapular-1": {
            "elevation": ["levator scapulae", "trapezius", "rhomboid"],
            "depression": ["trapezius", "lattisimus dorsi", "serratus anterior", "pectoralis"]
        },
        "scapular-2": {
            "protraction": ["serratus anterior", "pectoralis"],
            "retraction": ["trapezius", "lattisimus dorsi", "rhomboid"]
        },
        "humerus-1": {
            "abduction": ["supraspinatus", "deltoid", "trapezius", "serratus anterior"],
            "adduction": ["teres major", "pectoralis major"]
        },
        "humerus-2": {
            "medial rotation": ["subscapularis", "latissimus dorsi", "teres major", "pectoralis major"],
            "lateral rotation": ["infrascapular", "teres minor"]
        },
        "elbow joint": {
            "flexion": ["biceps brachii", "brachialis", "brachioradialis"],
            "extension": ["triceps brachii", "anconeus"]
        },
        "ulnarradial joint": {
            "pronation": ["pronator teres", "pronator quadratus"],
            "supination": ["supinator"]
        },
        "phalange": {
            "flexion": ["flexor digitorium", "flexor pollicis", "flexor digiti minimi brevis"],
            "extension": ["extensr digitorium", "extensor pollicis", "extensor digiti minimi"]
        },
        "wrist joint-1": {
            "flexion": ["flexor carpi", "palmaris longus"],
            "extension": ["extensor carpi radialis", "extensor carpi ulnaris"]
        },
        "wrist joint-2": {
            "abduction": ["flexor carpi radialis", "abductor pollicis", "extensor pollicis"],
            "adduction": ["flexor carpi ulnaris"]
        },
        "thumb": {
            "abduction": ["abductor pollicis"],
            "adduction": ["adductor pollicis"]
        },
        "hyper-thumb": {
            "abduction": ["abductor digiti minimi"],
            "adduction": ["palmar interosseous"]
        }
    }
    r =[*range(12)]
    random.shuffle(r)
    for i in range(12):
        v = [u for u in d][r[i]]
        print(v)
        z = d[v]
        print(*[j for j in z], sep = ', ')
        input()
        for j in z:
            print(j, z[j])
        print()

q6()
