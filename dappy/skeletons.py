CONNECTIVITY_DICT = {
    "mouse22": [
        (0, 1),
        (1, 2),
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (8, 9),
        (9, 10),
        (10, 11),
        (11, 3),
        (12, 13),
        (13, 14),
        (14, 15),
        (15, 3),
        (16, 17),
        (17, 18),
        (18, 4),
        (19, 20),
        (20, 21),
        (21, 4),
    ],
    "mouse20": [
        (0, 1),
        (1, 3),
        (0, 2),
        (2, 3),
        (2, 1),
        (0, 3),
        (4, 3),
        (5, 4),
        (6, 5),
        (7, 6),
        (8, 9),
        (9, 10),
        (10, 3),
        (11, 12),
        (12, 13),
        (13, 3),
        (14, 15),
        (15, 16),
        (16, 5),
        (17, 18),
        (18, 19),
        (19, 5),
    ],
    "mouse20_notail": [
        (0, 1),
        (1, 3),
        (0, 2),
        (2, 3),
        (2, 1),
        (0, 3),
        (4, 3),
        (5, 4),
        (6, 7),
        (7, 8),
        (8, 3),  # Connect to spinef
        (9, 10),
        (10, 11),
        (11, 3),  # Connect to spinef
        (12, 13),
        (13, 14),
        (14, 5),
        (15, 16),
        (16, 17),
        (17, 5),
    ],
    "mouse_abomination": [
        (0, 1),
        (1, 3),
        (0, 2),
        (2, 3),
        (2, 1),
        (0, 3),
        (4, 3),
        (5, 4),
        (6, 7),
        (7, 8),
        (8, 4),  # Connect to spinef
        (9, 10),
        (10, 11),
        (11, 4),  # Connect to spinef
    ],
    "NTUhuman": [
        (0, 1),
        (1, 20),
        (20, 2),
        (2, 3),
        (0, 16),
        (16, 17),
        (17, 18),
        (18, 19),
        (0, 12),
        (12, 13),
        (13, 14),
        (14, 15),
        (20, 8),
        (8, 9),
        (9, 10),
        (10, 11),
        (11, 23),
        (24, 11),
        (20, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 21),
        (7, 22),
    ],
    "rat_23": [
        (0, 1),
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 4),
        (0, 5),
        (5, 6),
        (1, 7),
        (7, 8),
        (8, 9),
        (9, 10),
        (1, 11),
        (11, 12),
        (12, 13),
        (13, 14),
        (5, 15),
        (15, 16),
        (16, 17),
        (17, 18),
        (5, 19),
        (19, 20),
        (20, 21),
        (21, 22),
    ],
}

COLOR_DICT = {
    "mouse22": [
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0.2609, 0, 0.5000),
        (1.0000, 0.5217, 0, 0.5000),
        (1.0000, 0.7826, 0, 0.5000),
        (0.9565, 1.0000, 0, 0.5000),
        (0.6957, 1.0000, 0, 0.5000),
        (0.4348, 1.0000, 0, 0.5000),
        (0.1739, 1.0000, 0, 0.5000),
        (0, 1.0000, 0.0870, 0.5000),
        (0, 1.0000, 0.3478, 0.5000),
        (0, 1.0000, 0.6087, 0.5000),
        (0, 1.0000, 0.8696, 0.5000),
        (0, 0.8696, 1.0000, 0.5000),
        (0, 0.6087, 1.0000, 0.5000),
        (0, 0.3478, 1.0000, 0.5000),
        (0, 0.0870, 1.0000, 0.5000),
        (0.1739, 0, 1.0000, 0.5000),
        (0.4348, 0, 1.0000, 0.5000),
        (0.6957, 0, 1.0000, 0.5000),
        (0.9565, 0, 1.0000, 0.5000),
        (1.0000, 0, 0.7826, 0.5000),
        (1.0000, 0, 0.5217, 0.5000),
        (1.0000, 0, 0.2609, 0.5000),
        (1.0000, 0, 0, 0.5000),
    ],
    "mouse20": [
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
    ],
    "mouse20_notail": [
        (1.0000, 0, 0, 0.5000),
        (0.9565, 1.0000, 0, 0.5000),
        (1.0000, 0.5217, 0, 0.5000),
        (0.6957, 1.0000, 0, 0.5000),
        (1.0000, 0.2609, 0, 0.5000),
        (1.0000, 0.7826, 0, 0.5000),
        (0.4348, 1.0000, 0, 0.5000),
        (0.1739, 1.0000, 0, 0.5000),
        (0, 1.0000, 0.6087, 0.5000),
        (0, 1.0000, 0.8696, 0.5000),
        (0, 0.6087, 1.0000, 0.5000),
        (0, 0.8696, 1.0000, 0.5000),
        (0, 0.3478, 1.0000, 0.5000),
        (0.4348, 0, 1.0000, 0.5000),
        (0.1739, 0, 1.0000, 0.5000),
        (0.6957, 0, 1.0000, 0.5000),
        (1.0000, 0, 0.7826, 0.5000),
        (0.9565, 0, 1.0000, 0.5000),
        (1.0000, 0, 0.5217, 0.5000),
        (1.0000, 0, 0.2609, 0.5000),
    ],
    #     [(1.0000, 0, 0, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (0, 0, 1.0000, 0.5000),
    #     (0, 0, 1.0000, 0.5000),
    #     (0, 0, 1.0000, 0.5000),
    #     (0, 0, 1.0000, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (1.0000, 0, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    #     (0, 1.0000, 0, 0.5000),
    # ],
    "mouse_abomination": [
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (0, 0, 1.0000, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
        (0, 1.0000, 0, 0.5000),
    ],
    "NTUhuman": [
        (0, 0, 0, 0.5),
        (0, 0, 0, 0.5),
        (0, 0, 0, 0.5),
        (0, 0, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0, 1, 0.5),
        (0, 0, 1, 0.5),
        (0, 0, 1, 0.5),
        (0, 0, 1, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
    ],
    "lafan": [
        (0, 0, 0, 0.5),
        (0, 0, 0, 0.5),
        (0, 0, 0, 0.5),
        (0, 0, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0.5, 0, 0.5),
        (0, 0, 1, 0.5),
        (0, 0, 1, 0.5),
        (0, 0, 1, 0.5),
        (0, 0, 1, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (1, 0, 0, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
        (0, 1, 1, 0.5),
    ],
    "rat_23": [
        (0.4348, 1.0000, 0, 0.5000),
        (1.0000, 0, 0, 0.5000),
        (0.9565, 1.0000, 0, 0.5000),
        (1.0000, 0.5217, 0, 0.5000),
        (0.6957, 1.0000, 0, 0.5000),
        (1.0000, 0.2609, 0, 0.5000),
        (1.0000, 0.7826, 0, 0.5000),
        (0.4348, 1.0000, 0, 0.5000),
        (0.1739, 1.0000, 0, 0.5000),
        (0, 1.0000, 0.6087, 0.5000),
        (0, 1.0000, 0.8696, 0.5000),
        (0, 1.0000, 0.8696, 0.5000),
        (0, 0.6087, 1.0000, 0.5000),
        (0, 0.3478, 1.0000, 0.5000),
        (0, 0.8696, 1.0000, 0.5000),
        (0, 0.8696, 1.0000, 0.5000),
        (0.4348, 0, 1.0000, 0.5000),
        (0.1739, 0, 1.0000, 0.5000),
        (0.6957, 0, 1.0000, 0.5000),
        (0.6957, 0, 1.0000, 0.5000),
        (1.0000, 0, 0.7826, 0.5000),
        (0.9565, 0, 1.0000, 0.5000),
        (1.0000, 0, 0.5217, 0.5000),
        (1.0000, 0, 0.2609, 0.5000),
        (1.0000, 0, 0.2609, 0.5000),
    ],
}

JOINT_NAME_DICT = {
    "mouse20": [
        "Snout",
        "EarR",
        "EarL",
        "SpineF",
        "SpineM",
        "Tail_base_",
        "Tail_mid_",
        "Tail_end_",
        "Forepaw_R",
        "Wrist_R",
        "ForeLimb_R",
        "Forepaw_L",
        "Wrist_L",
        "Forelimb_L",
        "Hindpaw_R",
        "Ankel_R",
        "Hindlimb_R",
        "Hindpaw_L",
        "Ankel_L",
        "Hindlimb_L",
    ],
    "mouse20_notail": [
        "Snout",  # 0
        "EarR",  # 1
        "EarL",  # 2
        "SpineF",  # 3
        "SpineM",  # 4
        "Tail_base_",  # 5
        "Forepaw_R",  # 6
        "Wrist_R",  # 7
        "ForeLimb_R",  # 8
        "Forepaw_L",  # 9
        "Wrist_L",  # 10
        "Forelimb_L",  # 11
        "Hindpaw_R",  # 12
        "Ankel_R",  # 13
        "Hindlimb_R",  # 14
        "Hindpaw_L",  # 15
        "Ankel_L",  # 16
        "Hindlimb_L",  # 17
    ],
    "mouse_abomination": [
        "Snout",
        "EarR",
        "EarL",
        "SpineF",
        "SpineM",
        "Tail_base_",
        "Paw_R",
        "Ankle_R",
        "Limb_R",
        "Paw_L",
        "Ankle_L",
        "Limb_L",
    ],
    "NTUhuman": [
        "Base",
        "SpineM",
        "Neck",
        "Head",
        "ShoulderL",
        "ElbowL",
        "WristL",
        "HandL",
        "ShoulderR",
        "ElbowR",
        "WristR",
        "HandR",
        "HipL",
        "KneeL",
        "AnkleL",
        "FootL",
        "HipR",
        "KneeR",
        "AnkleR",
        "FootR",
        "SpineF",
        "FingerL",
        "ThumbL",
        "FingerR",
        "ThumbR",
    ],
    "lafan": [
        "Hips",
        "LeftUpLeg",
        "LeftLeg",
        "LeftFoot",
        "LeftToe",
        "RightUpLeg",
        "RightLeg",
        "RightFoot",
        "RightToe",
        "Spine",
        "Spine1",
        "Spine2",
        "Neck",
        "Head",
        "LeftShoulder",
        "LeftArm",
        "LeftForeArm",
        "LeftHand",
        "RightShoulder",
        "RightArm",
        "RightForeArm",
        "RightHand",
    ],
    "rat_23": [
        "SpineM",  # 0
        "SpineF",  # 1
        "EarL",  # 2
        "EarR",  # 3
        "Snout",  # 4
        "SpineL",  # 5
        "TailBase",  # 6
        "ShoulderL",  # 7
        "ELbowL",  # 8
        "WristL",  # 9
        "HandL",  # 10
        "ShoulderR",  # 11
        "ELbowR",  # 12
        "WristR",  # 13
        "HandR",  # 14
        "HipL",  # 15
        "KneeL",  # 16
        "AnkleL",  # 17
        "FootL",  # 18
        "HipR",  # 19
        "KneeR",  # 20
        "AnkleR",  # 21
        "FootR",  # 22
    ],
}

JOINT_ANGLES_DICT = {
    # "mouse20_notail": [
    #     # Explicit connections
    #     (0, 1, 3),
    #     (0, 3, 4),
    #     (3, 4, 5),
    #     (3, 4, 8),
    #     (3, 8, 7),
    #     (8, 7, 6),
    #     (8, 4, 5),
    #     (3, 4, 11),
    #     (3, 11, 10),
    #     (11, 10, 9),
    #     (11, 4, 5),
    #     (4, 5, 14),
    #     (5, 14, 13),
    #     (14, 13, 12),
    #     (4, 5, 17),
    #     (5, 17, 16),
    #     (17, 16, 15),
    #     # Skip connections
    #     (0, 3, 7),
    #     (0, 3, 10),
    #     (0, 5, 13),
    #     (0, 5, 16),
    #     (7, 3, 10),
    #     (7, 4, 13),
    #     (7, 4, 16),
    #     (10, 4, 13),
    #     (10, 4, 16),
    # ],
    "mouse20_notail": [
        # Explicit connections
        (0, 1, 3),
        (0, 2, 3),
        (0, 3, 4),
        (1, 3, 4),
        (2, 3, 4),
        (3, 4, 5),
        (1, 3, 8),
        (2, 3, 8),
        (0, 3, 8),
        (3, 8, 7),
        (8, 7, 6),
        (1, 3, 11),
        (2, 3, 11),
        (0, 3, 11),
        (3, 11, 10),
        (11, 10, 9),
        (4, 5, 14),
        (5, 14, 13),
        (14, 13, 12),
        (4, 5, 17),
        (5, 17, 16),
        (17, 16, 15),
        # Skip connections
        (0, 3, 6),
        (0, 3, 7),
        (0, 3, 9),
        (0, 3, 10),
        (4, 5, 12),
        (4, 5, 13),
        (4, 5, 15),
        (4, 5, 16),
    ],
    "mouse_abomination": [
        # Explicit connections
        (0, 1, 3),
        (0, 3, 4),
        (3, 4, 5),
        (3, 4, 8),
        (3, 8, 7),
        (8, 7, 6),
        (8, 4, 5),
        (3, 4, 11),
        (3, 11, 10),
        (11, 10, 9),
        (11, 4, 5),
        # Skip connections
        (0, 4, 7),
        (0, 4, 10),
    ],
    "NTUhuman": [
        # Explicit connections
        (3, 2, 20),
        (2, 20, 1),
        (20, 1, 0),
        (1, 0, 12),
        (0, 12, 13),
        (12, 13, 14),
        (13, 14, 15),
        (1, 0, 16),
        (0, 16, 17),
        (16, 17, 18),
        (17, 18, 19),
        (1, 20, 4),
        (20, 4, 5),
        (4, 5, 6),
        (5, 6, 7),
        (1, 20, 8),
        (20, 8, 9),
        (8, 9, 10),
        (9, 10, 11),
        (16, 0, 12),
        # hand angles
        # (10,11,23),
        # (10,11,24),
        # (24,11,23),
        # (6,7,21),
        # (6,7,22),
        # (22,7,21),
        # Skip connections
        (3, 20, 6),
        (3, 20, 10),
        (3, 0, 14),
        (3, 0, 18),
        (6, 1, 14),
        (6, 1, 18),
        (10, 1, 14),
        (10, 1, 18),
    ],
    "lafan": [
        # Explicit connections
        (3, 2, 20),
        (2, 20, 1),
        (20, 1, 0),
        (1, 0, 12),
        (0, 12, 13),
        (12, 13, 14),
        (13, 14, 15),
        (1, 0, 16),
        (0, 16, 17),
        (16, 17, 18),
        (17, 18, 19),
        (1, 20, 4),
        (20, 4, 5),
        (4, 5, 6),
        (5, 6, 7),
        (1, 20, 8),
        (20, 8, 9),
        (8, 9, 10),
        (9, 10, 11),
        (16, 0, 12),
        # Skip connections
        (3, 20, 6),
        (3, 20, 10),
        (3, 0, 14),
        (3, 0, 18),
        (6, 1, 14),
        (6, 1, 18),
        (10, 1, 14),
        (10, 1, 18),
    ],
    "rat_23": [
        # Explicit connections
        (4, 1, 0),
        (4, 3, 1),
        (4, 2, 1),
        (2, 1, 0),
        (3, 1, 0),
        (1, 0, 5),
        (0, 5, 6),
        (2, 1, 7),
        (3, 1, 7),
        (4, 1, 7),
        (1, 7, 8),
        (7, 8, 9),
        (8, 9, 10),
        (2, 1, 11),
        (3, 1, 11),
        (4, 1, 11),
        (1, 11, 12),
        (11, 12, 13),
        (12, 13, 14),
        (0, 5, 15),
        (5, 15, 16),
        (15, 16, 17),
        (16, 17, 18),
        (15, 5, 6),
        (0, 5, 19),
        (5, 19, 20),
        (19, 20, 21),
        (20, 21, 22),
        (19, 5, 6),
        # Skip connections
        (4, 1, 8),
        (4, 1, 9),
        (4, 1, 10),
        (4, 1, 12),
        (4, 1, 13),
        (4, 1, 14),
        (0, 5, 16),
        (0, 5, 17),
        (0, 5, 18),
        (0, 5, 20),
        (0, 5, 21),
        (0, 5, 22),
    ],
}
