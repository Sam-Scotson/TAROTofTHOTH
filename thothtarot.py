class ThothTarotCard:
    def __init__(self, number, zodiac_sign, planet, hebrew_letter, position_on_tree, assigned_colors, summary):
        self.number = number
        self.zodiac_sign = zodiac_sign
        self.planet = planet
        self.hebrew_letter = hebrew_letter
        self.position_on_tree = position_on_tree
        self.assigned_colors = assigned_colors
        self.summary = summary
fire_suite = {
    "Ace of Wands": ThothTarotCard(
        number=1,
        zodiac_sign="Elemental Trump of Fire",
        planet="Sun",
        hebrew_letter="Yod (י) - Hand or Virgo",
        position_on_tree="Path 32 (Yesod to Malkuth) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Orange - Symbolizing Creativity, Inspiration, and Vitality",
        summary="The Ace of Wands embodies the pure potential of creative energy. It signifies new beginnings, inspiration, and the spark of passion. This card encourages us to embrace our creative impulses, take initiative, and manifest our desires in the material world."
    ),
    "Two of Wands": ThothTarotCard(
        number=2,
        zodiac_sign="Mars in Aries",
        planet="Mars",
        hebrew_letter="Heh (ה) - Window or Aries",
        position_on_tree="Path 12 (Kether to Chokmah) - The Path of Pure Intelligence",
        assigned_colors="Red, Dominion Yellow - Representing Willpower, Expansion, and Potential",
        summary="The Two of Wands represents the power of will and the potential for manifestation. It signifies the initial stages of planning and the courage to take action. This card encourages us to assert our authority, make strategic decisions, and embrace opportunities for growth."
    ),
    "Three of Wands": ThothTarotCard(
        number=3,
        zodiac_sign="Sun in Aries",
        planet="Sun",
        hebrew_letter="Vav (ו) - Nail or Taurus",
        position_on_tree="Path 14 (Binah to Chokmah) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Virtue Blue - Symbolizing Exploration, Expansion, and Confidence",
        summary="The Three of Wands represents the expansion of creative vision and the anticipation of success. It signifies the ability to foresee opportunities and take proactive steps toward realizing goals. This card encourages us to have faith in our abilities, explore new horizons, and manifest our aspirations."
    ),
    "Four of Wands": ThothTarotCard(
        number=4,
        zodiac_sign="Venus in Aries",
        planet="Venus",
        hebrew_letter="Zayin (ז) - Weapon or Gemini",
        position_on_tree="Path 16 (Chesed to Geburah) - The Path of Pure Intelligence",
        assigned_colors="Red, Chesed Blue - Representing Celebration, Harmony, and Stability",
        summary="The Four of Wands embodies the joy of celebration and harmonious relationships. It signifies a time of stability, harmony, and alignment with others. This card encourages us to come together with a sense of unity, express gratitude for our achievements, and build strong foundations."
    ),
    "Five of Wands": ThothTarotCard(
        number=5,
        zodiac_sign="Saturn in Leo",
        planet="Saturn",
        hebrew_letter="Cheth (ח) - Fence or Cancer",
        position_on_tree="Path 18 (Geburah to Tiphareth) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Geburah Red - Symbolizing Competition, Struggle, and Growth",
        summary="The Five of Wands represents challenges and competition that foster growth and development. It signifies conflicts and obstacles that lead to inner strength and self-discovery. This card encourages us to embrace challenges, learn from conflicts, and harness the transformative power of adversity."
    ),
    "Six of Wands": ThothTarotCard(
        number=6,
        zodiac_sign="Jupiter in Leo",
        planet="Jupiter",
        hebrew_letter="Teth (ט) - Serpent or Leo",
        position_on_tree="Path 20 (Tiphareth to Chesed) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Victory Orange - Representing Triumph, Recognition, and Leadership",
        summary="The Six of Wands embodies victory, recognition, and the attainment of goals. It signifies a time of achievement and the acknowledgment of one's efforts. This card encourages us to celebrate our successes, embrace leadership roles, and inspire others through our accomplishments."
    ),
    "Seven of Wands": ThothTarotCard(
        number=7,
        zodiac_sign="Mars in Leo",
        planet="Mars",
        hebrew_letter="Yod (י) - Hand or Virgo",
        position_on_tree="Path 22 (Chokmah to Tiphareth) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Valour Orange - Symbolizing Courage, Determination, and Persistence",
        summary="The Seven of Wands represents the courage to defend one's position and stand up for beliefs. It signifies challenges that require inner strength and resilience. This card encourages us to assert our boundaries, overcome opposition, and maintain our integrity in the face of adversity."
    ),
    "Eight of Wands": ThothTarotCard(
        number=8,
        zodiac_sign="Mercury in Sagittarius",
        planet="Mercury",
        hebrew_letter="Kaph (כ) - Fist or Jupiter",
        position_on_tree="Path 24 (Tiphareth to Netzach) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Swiftness Orange - Representing Expansion, Speed, and Rapid Progress",
        summary="The Eight of Wands embodies swift progress, communication, and dynamic movement. It signifies the rapid unfolding of plans and the exchange of ideas. This card encourages us to embrace opportunities that propel us forward, communicate effectively, and maintain a sense of enthusiasm."
    ),
    "Nine of Wands": ThothTarotCard(
        number=9,
        zodiac_sign="Moon in Sagittarius",
        planet="Moon",
        hebrew_letter="Teth (ט) - Serpent or Leo",
        position_on_tree="Path 26 (Geburah to Hod) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Great Strength Orange - Symbolizing Perseverance, Resilience, and Determination",
        summary="The Nine of Wands represents inner strength, resilience, and the ability to overcome challenges. It signifies a test of one's endurance and the willingness to stand firm. This card encourages us to persevere in the face of adversity, draw upon our inner resources, and maintain our determination."
    ),
    "Ten of Wands": ThothTarotCard(
        number=10,
        zodiac_sign="Saturn in Sagittarius",
        planet="Saturn",
        hebrew_letter="Resh (ר) - Head or Sun",
        position_on_tree="Path 28 (Netzach to Netzach) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Oppression Orange - Representing Burden, Responsibility, and Completion",
        summary="The Ten of Wands embodies the weight of responsibility and the completion of a cycle. It signifies the burdens that result from ambition and the need to release unnecessary baggage. This card encourages us to assess our commitments, delegate tasks, and free ourselves from self-imposed limitations."
    ),
    "Princess of Wands": ThothTarotCard(
        number=11,
        zodiac_sign="Leo and Cancer",
        planet="Earth",
        hebrew_letter="Shin (ש) - Tooth or Fire",
        position_on_tree="Path 30 (Netzach to Malkuth) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Rose - Symbolizing Exploration, Passion, and Enthusiasm",
        summary="The Princess of Wands embodies the spirit of exploration and curiosity. She represents youthful energy, creativity, and the willingness to embrace new experiences. This card encourages us to approach life with enthusiasm, express our passions freely, and embark on journeys of self-discovery."
    ),
    "Prince of Wands": ThothTarotCard(
        number=12,
        zodiac_sign="Leo and Cancer",
        planet="Aries",
        hebrew_letter="Nun (נ) - Fish or Scorpio",
        position_on_tree="Path 14 (Binah to Chokmah) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Fiery Orange - Representing Enthusiasm, Leadership, and Courage",
        summary="The Prince of Wands embodies dynamic leadership and the courage to take initiative. He represents the fiery spirit of adventure and the ability to overcome obstacles. This card encourages us to pursue our goals with enthusiasm, assert our authority, and embrace opportunities for growth."
    ),
    "Queen of Wands": ThothTarotCard(
        number=13,
        zodiac_sign="Aries and Pisces",
        planet="Water",
        hebrew_letter="Resh (ר) - Head or Sun",
        position_on_tree="Path 16 (Chesed to Geburah) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Warm Orange - Symbolizing Intuition, Charisma, and Creative Expression",
        summary="The Queen of Wands embodies intuitive wisdom and charismatic energy. She represents the balance of intuition and creativity, and the ability to inspire others. This card encourages us to trust our inner guidance, express our passions authentically, and radiate our unique light."
    ),
    "Knight of Wands": ThothTarotCard(
        number=14,
        zodiac_sign="Aries and Pisces",
        planet="Air",
        hebrew_letter="Shin (ש) - Tooth or Fire",
        position_on_tree="Path 18 (Geburah to Tiphareth) - The Path of Pure Intelligence",
        assigned_colors="Yellow, Brilliant Orange - Representing Action, Enthusiasm, and Exploration",
        summary="The Knight of Wands embodies adventurous spirit and the pursuit of new horizons. He represents the courage to explore uncharted territories and embrace challenges. This card encourages us to take bold action, channel our energy into creative endeavors, and fearlessly venture into the unknown."
    ),
}
air_suite = {
    "Ace of Swords": ThothTarotCard(
        number=1,
        zodiac_sign="Element of Air",
        planet="Mercury",
        hebrew_letter="Aleph (א) - Air",
        position_on_tree="Path 11 (Kether to Chokmah) - The Path of Potential",
        assigned_colors="Bright Yellow, Pale Gray, Azure - Representing Clarity, New Beginnings, and Inspiration",
        summary="The Ace of Swords signifies the seed of clear perception and focused intellect. It is the primal force of the Air element, representing the power of thought and communication. This card invites us to tap into our mental clarity and use it as a tool to cut through confusion and gain insight."
    ),
    "Two of Swords": ThothTarotCard(
        number=2,
        zodiac_sign="Moon in Libra",
        planet="Moon",
        hebrew_letter="Cheth (ח) - Fence or Cancer",
        position_on_tree="Path 18 (Geburah to Binah) - The Path of Triumph",
        assigned_colors="Indigo, Black and White - Signifying Balance, Duality, and Equilibrium",
        summary="The Two of Swords depicts a balance between opposing forces, suggesting a need for decisions and choices. It represents the power of equilibrium and encourages us to find harmony between different aspects of our lives. This card reminds us that clear judgment is necessary to make balanced decisions."
    ),
    "Three of Swords": ThothTarotCard(
        number=3,
        zodiac_sign="Saturn in Libra",
        planet="Saturn",
        hebrew_letter="Kaph (כ) - Fist or Jupiter",
        position_on_tree="Path 22 (Chokmah to Tiphareth) - The Path of Balance",
        assigned_colors="Deep Red, Black and Gray - Symbolizing Suffering, Transformation, and Equilibrium",
        summary="The Three of Swords portrays sorrow and heartbreak caused by the transformational energies of Saturn. It signifies the need to face pain and discomfort to achieve growth and balance. This card encourages us to embrace our wounds as opportunities for transformation and healing."
    ),
    "Four of Swords": ThothTarotCard(
        number=4,
        zodiac_sign="Jupiter in Libra",
        planet="Jupiter",
        hebrew_letter="Lamed (ל) - Ox Goad or Libra",
        position_on_tree="Path 22 (Chokmah to Tiphareth) - The Path of Balance",
        assigned_colors="Pale Blue, Emerald Green - Representing Rest, Healing, and Equilibrium",
        summary="The Four of Swords depicts a state of rest and healing after a period of struggle. It signifies the need for introspection and recuperation, allowing the mind to regain clarity and strength. This card reminds us of the importance of balance and the restoration of equilibrium in our lives."
    ),
    "Five of Swords": ThothTarotCard(
        number=5,
        zodiac_sign="Venus in Aquarius",
        planet="Venus",
        hebrew_letter="Heh (ה) - Window or Aries",
        position_on_tree="Path 18 (Geburah to Binah) - The Path of Triumph",
        assigned_colors="Emerald Green, Turquoise - Symbolizing Conflict, Change, and Rebirth",
        summary="The Five of Swords represents conflict and change within the realm of thought and communication. It suggests that overcoming challenges requires adapting our perspectives. This card teaches us the importance of embracing change and releasing attachments to rigid beliefs."
    ),
    "Six of Swords": ThothTarotCard(
        number=6,
        zodiac_sign="Mercury in Aquarius",
        planet="Mercury",
        hebrew_letter="Vav (ו) - Nail or Taurus",
        position_on_tree="Path 18 (Geburah to Binah) - The Path of Triumph",
        assigned_colors="Light Blue, Emerald Green - Representing Transition, Communication, and Healing",
        summary="The Six of Swords signifies transition and moving away from difficulty toward calmer waters. It symbolizes the healing power of communication and the journey of the mind from turbulence to tranquility. This card encourages us to seek solace in intellectual and emotional growth."
    ),
    "Seven of Swords": ThothTarotCard(
        number=7,
        zodiac_sign="Moon in Aquarius",
        planet="Moon",
        hebrew_letter="Zayin (ז) - Weapon or Gemini",
        position_on_tree="Path 18 (Geburah to Binah) - The Path of Triumph",
        assigned_colors="Pale Blue, White - Symbolizing Strategy, Illusion, and Intuition",
        summary="The Seven of Swords represents strategic thinking and the duality of illusion and insight. It encourages us to navigate situations with cleverness while staying aware of potential deception. This card reminds us to trust our intuition and inner guidance when faced with challenges."
    ),
    "Eight of Swords": ThothTarotCard(
        number=8,
        zodiac_sign="Jupiter in Gemini",
        planet="Jupiter",
        hebrew_letter="Cheth (ח) - Fence or Cancer",
        position_on_tree="Path 18 (Geburah to Binah) - The Path of Triumph",
        assigned_colors="Orange, Olive Green - Signifying Limitation, Expansion, and Inner Reflection",
        summary="The Eight of Swords depicts the self-imposed limitations of the mind and the potential for growth through self-awareness. It encourages us to examine our thought patterns and beliefs that hold us back. This card teaches us that liberation from mental constraints begins with self-reflection."
    ),
    "Nine of Swords": ThothTarotCard(
        number=9,
        zodiac_sign="Mars in Gemini",
        planet="Mars",
        hebrew_letter="Teth (ט) - Serpent or Leo",
        position_on_tree="Path 18 (Geburah to Binah) - The Path of Triumph",
        assigned_colors="Red, Blue - Representing Anxiety, Action, and Spiritual Insight",
        summary="The Nine of Swords represents anxiety and mental distress caused by overthinking. It invites us to take action and confront our fears instead of succumbing to them. This card reminds us of the power of transforming negative thoughts into spiritual insight and inner strength."
    ),
    "Ten of Swords": ThothTarotCard(
        number=10,
        zodiac_sign="Sun in Gemini",
        planet="Sun",
        hebrew_letter="Yod (י) - Hand or Virgo",
        position_on_tree="Path 20 (Tiphareth to Chesed) - The Path of Divine Light",
        assigned_colors="Dark Gray, Maroon - Signifying Transformation, Endings, and Renewal",
        summary="The Ten of Swords represents a painful ending or transformation that leads to new beginnings. It signifies the completion of a cycle and the potential for renewal after experiencing difficulties. This card teaches us to embrace change and find hope in the darkest moments."
    ),
    "Princess of Swords": ThothTarotCard(
        number=11,
        zodiac_sign="Element of Air",
        planet="Mars",
        hebrew_letter="Heh (ה) - Window or Aries",
        position_on_tree="Path 15 (Chesed to Geburah) - The Path of Discipline",
        assigned_colors="Pale Blue, Bright Yellow - Representing Communication, Curiosity, and Clarity",
        summary="The Princess of Swords embodies youthful curiosity and intellect. She represents the thirst for knowledge and the power of open-minded communication. This card encourages us to embrace learning and exploration as well as maintain clarity in our thoughts and words."
    ),
    "Prince of Swords": ThothTarotCard(
        number=12,
        zodiac_sign="Aquarius and Capricorn",
        planet="Neptune",
        hebrew_letter="Teth (ט) - Serpent or Leo",
        position_on_tree="Path 27 (Netzach to Hod) - The Path of Natural Intelligence",
        assigned_colors="Deep Purple, Azure - Symbolizing Intuition, Practicality, and Inspiration",
        summary="The Prince of Swords embodies the balanced use of intellect and intuition. He represents intellectual curiosity grounded in practical application. This card encourages us to use our mental faculties to bring inspiration into reality and to harness the power of both logic and intuition."
    ),
    "Queen of Swords": ThothTarotCard(
        number=13,
        zodiac_sign="Gemini and Taurus",
        planet="Moon",
        hebrew_letter="Nun (נ) - Fish or Scorpio",
        position_on_tree="Path 29 (Netzach to Malkuth) - The Path of Natural Stability",
        assigned_colors="Violet, Blue - Signifying Wisdom, Intuition, and Spiritual Insights",
        summary="The Queen of Swords embodies wisdom and the ability to cut through illusion to access deeper truths. She represents the balance of intuition and intellect and encourages us to trust our inner guidance. This card invites us to seek spiritual insights and make decisions rooted in clarity."
    ),
    "Knight of Swords": ThothTarotCard(
        number=14,
        zodiac_sign="Gemini and Taurus",
        planet="Saturn",
        hebrew_letter="Samekh (ס) - Prop or Sagittarius",
        position_on_tree="Path 31 (Hod to Yesod) - The Path of Natural Perfection",
        assigned_colors="Pale Blue, Violet - Representing Skill, Precision, and Spiritual Quest",
        summary="The Knight of Swords embodies the quest for spiritual truths and the dedication to mastering one's skills. He represents the pursuit of wisdom and the balance between seeking knowledge and practicing discipline. This card encourages us to refine our abilities and embark on a spiritual journey with determination."
    ),
}

Major_Arcana={
    "The Fool": ThothTarotCard(
        "Number": 0,
        "Zodiac Sign": "Joker",
        "Planet": "All",
        "Hebrew Letter": "Aleph (א) - Air",
        "Position on Tree": "Path 11 (Kether to Chokmah) - The Path of Potential",
        "Assigned Colors": "Multicolored - Reflecting Infinite Possibilities and Divine Potential",
        "Summary": "The Fool card holds a profound significance as the card of zero, representing both the unmanifest potential and the point of origin from which all other cards emanate. It symbolizes the primal, unconditioned state of existence, akin to the 'Ein Sof' or limitless divine potential. The Fool is in direct connection to Kether, the Crown, the highest Sephirah on the Tree of Life, signifying the spark of divine consciousness that initiates creation.\n\nIn the context of the hero's journey, The Fool embodies the archetype of the adventurer setting forth into the unknown. The Fool's innocence and fearlessness reflect the beginning of a transformative voyage, encountering challenges and growth along the way. This card reminds us of the boundless possibilities present when we step outside our comfort zones and embark on our personal quests.The Joker archetype represents the completely deconditioned mind, enabling the state of 'Samadhi' or the equanimous mindset. This card embodies the ultimate liberation from mental constructs and societal influences, allowing the individual to transcend biases, attachments, and distractions. In the context of the Tarot, the Joker signifies the pinnacle of spiritual awareness, where the fluctuations of the mind are stilled, and a profound sense of inner calm and clarity prevails. The Joker's presence invites us to embrace a state of serene detachment, where we observe the ebb and flow of life without judgment or emotional entanglement, and instead, cultivate a balanced perspective that aligns with our higher self"
    ),
    "The Magus": {
        "Number": 1,
        "Zodiac Sign": "Messagner of the God's",
        "Planet": "Mercury",
        "Hebrew Letter": "Beth (ב) - House or Mercury",
        "Position on Tree": "Path 12 (Kether to Binah) - The Path of Consciousness",
        "Assigned Colors": "Yellow and Purple - Blending Intellect and Spirituality",
        "Summary": "The Magus card embodies the archetype of the divine messenger and magician. Representing the power of communication and manipulation, it signifies the harmonious union of the spiritual and material realms. The Magus wields the four elements, symbolizing mastery over the natural forces.\n\nAs the path between Kether and Binah, this card represents the transfer of divine inspiration and creative potential to the receptive and structured realm of understanding. The Magus invites us to channel our inner potential into conscious action, reminding us that our thoughts, words, and actions shape our reality."
    },
    "The Priestess": {
        "Number": 2,
        "Zodiac Sign": "Trump of the Moon",
        "Planet": "Moon",
        "Hebrew Letter": "Gimel (ג) - Camel or Moon",
        "Position on Tree": "Path 13 (Kether to Tiphareth) - The Path of Understanding",
        "Assigned Colors": "Blue and Silver - Symbolizing Intuition and Mysteries",
        "Summary": "The Priestess card is a representation of the subconscious, intuition, and the hidden aspects of existence. She stands at the threshold of the unknown, embodying the mystery of the unmanifest potential. The Priestess is both a guide to the inner realms and a guardian of esoteric knowledge.\n\nAs the bridge between Kether and Tiphareth, she serves as the mediator between the divine source and the individual soul. The Priestess invites us to explore our inner landscapes, embrace our intuition, and trust the wisdom that arises from the depths of our being. This card symbolizes the delicate balance between light and shadow, revealing the power of inner reflection and the mysteries of the moonlit path."
    },
    "The Empress": {
        "Number": 3,
        "Zodiac Sign": "Venus",
        "Planet": "Earth",
        "Hebrew Letter": "Daleth (ד) - Door or Venus",
        "Position on Tree": "Path 14 (Binah to Chokmah) - The Path of Connection",
        "Assigned Colors": "Green and Blue - Representing Nature's Abundance and Emotional Depths",
        "Summary": "The Empress card embodies the essence of nurturing and fertility, representing the Divine Feminine and the creative force of nature. She is a symbol of abundance, growth, and the birthing of new life. As the embodiment of Venus, The Empress radiates the energy of love, beauty, and sensuality.\n\nSituated on the path between Binah and Chokmah, The Empress mediates the maternal and paternal aspects of the Tree of Life. She encourages us to connect with our intuitive and nurturing sides, embrace the cycles of creation, and appreciate the beauty and richness of the physical world. This card reminds us of our capacity to care for ourselves and others with unconditional love."
    },
    "The Emperor": {
        "Number": 4,
        "Zodiac Sign": "Aries",
        "Planet": "Mars",
        "Hebrew Letter": "Heh (ה) - Window or Aries",
        "Position on Tree": "Path 15 (Chesed to Geburah) - The Path of Discipline",
        "Assigned Colors": "Red and Yellow - Signifying Power, Leadership, and Determination",
        "Summary": "The Emperor card embodies the qualities of authority, leadership, and structure, reflecting the archetype of the Divine Masculine in its active and assertive form. As the embodiment of Mars, The Emperor exudes courage, determination, and the will to take action.\n\nOn the path between Chesed and Geburah, The Emperor serves as a bridge between expansion and restriction. He invites us to establish order, set boundaries, and exercise our power responsibly. This card symbolizes the importance of balance between asserting our authority and respecting the rights and needs of others. The Emperor encourages us to take charge of our lives and manifest our visions with discipline and strength."
    },
    "The Hierophant": {
        "Number": 5,
        "Zodiac Sign": "Taurus",
        "Planet": "Jupiter",
        "Hebrew Letter": "Vav (ו) - Nail or Taurus",
        "Position on Tree": "Path 16 (Chesed to Tiphareth) - The Path of Spiritual Connection",
        "Assigned Colors": "Yellow and Blue - Representing Divine Wisdom and Spiritual Harmony",
        "Summary": "The Hierophant card embodies spiritual guidance, tradition, and the transmission of divine wisdom. He represents the bridge between the earthly and spiritual realms, serving as a conduit for higher teachings and sacred rituals. The Hierophant is a symbol of religious and spiritual authority.\n\nAs a path between Chesed and Tiphareth, The Hierophant integrates spiritual values with compassionate action. This card invites us to seek guidance from spiritual traditions, honor our inner wisdom, and embrace the role of mentor and seeker. The Hierophant reminds us that connection to the divine can be found through both external teachings and inner exploration."
    },
    "The Lovers": {
        "Number": 6,
        "Zodiac Sign": "Gemini",
        "Planet": "Mercury",
        "Hebrew Letter": "Zayin (ז) - Weapon or Gemini",
        "Position on Tree": "Path 17 (Geburah to Tiphareth) - The Path of Integration",
        "Assigned Colors": "Red and Blue - Symbolizing Love, Choices, and Unity",
        "Summary": "The Lovers card represents the harmony and integration of opposing forces. It embodies the concept of duality and the potential for union and balance. The Lovers card speaks to the deep connections we form, whether in relationships, choices, or inner struggles.\n\nAs a path between Geburah and Tiphareth, The Lovers card signifies the transformative journey from severity to beauty. This card encourages us to make choices that align with our values and higher selves, fostering unity within and without. The Lovers remind us that true love and union are rooted in authenticity and the recognition of our interconnectedness."
    },
    "The Chariot": {
        "Number": 7,
        "Zodiac Sign": "Cancer",
        "Planet": "Moon",
        "Hebrew Letter": "Cheth (ח) - Fence or Cancer",
        "Position on Tree": "Path 18 (Geburah to Binah) - The Path of Triumph",
        "Assigned Colors": "Blue and Silver - Reflecting Determination and Emotional Balance",
        "Summary": "The Chariot card represents triumph, willpower, and the journey of the soul. It symbolizes the harmony between conscious and unconscious forces that propel us forward. The Chariot embodies controlled determination and the ability to overcome challenges through focused intention. This card urges us to align our will with higher purpose, guiding us through the trials of life with courage and the conviction to achieve our goals."
    },
    "Adjustment": {
        "Number": 8,
        "Zodiac Sign": "Libra",
        "Planet": "Venus",
        "Hebrew Letter": "Lamed (ל) - Ox Goad or Libra",
        "Position on Tree": "Path 22 (Chokmah to Tiphareth) - The Path of Balance",
        "Assigned Colors": "Blue and Green - Signifying Justice, Harmony, and Balance",
        "Summary": "The Adjustment card represents balance, justice, and the equilibrium of forces. It symbolizes the law of cause and effect, reflecting the cosmic principle that every action has consequences. Adjustment calls for the harmonization of opposing energies, leading to personal transformation and growth. This card reminds us to weigh our decisions carefully and to embrace the innate wisdom that governs the natural order of the universe."
    },
    "The Hermit": {
        "Number": 9,
        "Zodiac Sign": "Virgo",
        "Planet": "Mercury",
        "Hebrew Letter": "Yod (י) - Hand or Virgo",
        "Position on Tree": "Path 20 (Tiphareth to Chesed) - The Path of Divine Light",
        "Assigned Colors": "Gray and Indigo - Symbolizing Introspection and Inner Guidance",
        "Summary": "The Hermit card represents introspection, inner guidance, and solitude. It symbolizes the pursuit of inner wisdom and the illumination of one's path through self-discovery. The Hermit invites us to withdraw from external distractions and seek answers within. This card emphasizes the importance of self-reflection, contemplation, and the quest for deeper understanding. The Hermit's lantern shines a light on the hidden realms of the psyche, guiding us on a transformative journey of self-awareness."
    },
    "The Wheel of Fortune": {
        "Number": 10,
        "Zodiac Sign": "Jupiter",
        "Planet": "Jupiter",
        "Hebrew Letter": "Kaph (כ) - Fist or Jupiter",
        "Position on Tree": "Path 21 (Chesed to Netzach) - The Path of Fortune",
        "Assigned Colors": "Purple and Blue - Reflecting Cycles and Cosmic Harmony",
        "Summary": "The Wheel of Fortune card represents cycles, destiny, and the ever-changing nature of life. It symbolizes the continuous movement of existence, where circumstances and experiences shift in a cyclical fashion. The Wheel of Fortune reminds us of the interconnectedness of all things and the inevitability of change. This card teaches us to embrace the ebb and flow of life, finding wisdom in both the ups and downs, and to navigate the wheel with grace and acceptance."
    },
    "The Lust": {
        "Number": 11,
        "Zodiac Sign": "Leo",
        "Planet": "Sun",
        "Hebrew Letter": "Teth (ט) - Serpent or Leo",
        "Position on Tree": "Path 19 (Tiphareth to Geburah) - The Path of Raw Energy",
        "Assigned Colors": "Orange and Blue - Symbolizing Passion and Transformative Power",
        "Summary": "The Lust card represents the raw and primal forces of desire, passion, and creative energy. It embodies the fire within us that drives our actions and fuels our ambitions. This card signifies the harmonious union of opposites, where strength is harnessed through love and conscious choice. The Lust card challenges us to balance our primal instincts with our higher self, transforming base desires into expressions of divine creativity."
    },
    "The Hanged Man": {
        "Number": 12,
        "Zodiac Sign": "Neptune",
        "Planet": "Neptune",
        "Hebrew Letter": "Mem (מ) - Water",
        "Position on Tree": "Path 23 (Geburah to Hod) - The Path of Surrender and Reflection",
        "Assigned Colors": "Blue and Green - Representing Suspension and Illumination",
        "Summary": "The Hanged Man card represents surrender, self-sacrifice, and a shift in perspective. It symbolizes a voluntary letting go of control and the suspension of ordinary reality. By embracing the unknown and relinquishing attachment to outcomes, we gain new insights and open ourselves to spiritual growth. The Hanged Man encourages us to view challenges from a different angle, finding wisdom and transformation in moments of surrender."
    },
    "Art": {
        "Number": 14,
        "Zodiac Sign": "Sagittarius",
        "Planet": "Sagittarius",
        "Hebrew Letter": "Samekh (ס) - Support or Sagittarius",
        "Position on Tree": "Path 25 (Hod to Yesod) - The Path of Transformation",
        "Assigned Colors": "Red and Blue - Symbolizing Alchemical Fusion",
        "Summary": "The Art card represents the alchemical fusion of opposites to create balance and transformation. It symbolizes the synthesis of diverse elements within ourselves, leading to harmony and healing. Through the integration of conscious and unconscious energies, we become agents of personal and collective evolution. The Art card invites us to engage in the process of self-transmutation, discovering the hidden potentials within and transcending limitations."
    },
    "The Devil": {
        "Number": 15,
        "Zodiac Sign": "Capricorn",
        "Planet": "Saturn",
        "Hebrew Letter": "Ayin (ע) - Eye or Capricorn",
        "Position on Tree": "Path 26 (Geburah to Hod) - The Path of Liberation from Illusions",
        "Assigned Colors": "Indigo and Black - Signifying Temptation and Liberation",
        "Summary": "The Devil card represents materialism, bondage, and the illusions that hold us captive. It symbolizes the seductive nature of attachments and the fear-based patterns that keep us trapped. This card challenges us to confront our limitations and break free from self-imposed chains. By recognizing our shadow aspects and shedding false beliefs, we can liberate ourselves from the ego's control and reclaim our authentic power."
    },
        "The Tower": {
        "Number": 16,
        "Zodiac Sign": "Mars",
        "Planet": "Mars",
        "Hebrew Letter": "Peh (פ) - Mouth or Mars",
        "Position on Tree": "Path 27 (Netzach to Hod) - The Path of Destruction",
        "Assigned Colors": "Red and Blue - Symbolizing Transformation and Clarity Amid Chaos",
        "Summary": "The Tower card represents sudden upheaval, chaos, and the destruction of old structures. It symbolizes the breaking down of false foundations to make way for renewal and transformation. This card encourages us to embrace change, no matter how disruptive it may seem, as it paves the way for growth and evolution. The Tower reminds us that even in times of crisis, we can find opportunity and release ourselves from what no longer serves our highest good."
    },
    "The Star": {
        "Number": 17,
        "Zodiac Sign": "Aquarius",
        "Planet": "Uranus",
        "Hebrew Letter": "Tzaddi (צ) - Fish Hook or Aquarius",
        "Position on Tree": "Path 28 (Netzach to Yesod) - The Path of Meditation",
        "Assigned Colors": "Blue and Purple - Representing Inner Wisdom and Spiritual Connection",
        "Summary": "The Star card represents hope, inspiration, and spiritual guidance. It symbolizes the connection between the earthly and the divine. Just as stars illuminate the night sky, this card invites us to find light within ourselves even in the darkest of times. The Star encourages us to trust in our inner wisdom and intuition, guiding us towards a sense of renewal and inspiration. It signifies a period of healing and transformation, reminding us that even after challenges, there is always the promise of a new and brighter future."
    },
    "The Moon": {
        "Number": 18,
        "Zodiac Sign": "Pisces",
        "Planet": "Neptune",
        "Hebrew Letter": "Qoph (ק) - Back of the Head or Pisces",
        "Position on Tree": "Path 29 (Netzach to Malkuth) - The Path of Dreams",
        "Assigned Colors": "Blue and Silver - Reflecting Emotions and Signifying Mystery",
        "Summary": "The Moon card represents intuition, illusion, and the mysteries of the unconscious mind. It symbolizes the hidden aspects of reality that shape our perceptions. Like the moon's changing phases, this card calls us to explore the ebb and flow of our emotions and instincts. The Moon card invites us to trust our inner guidance, even when circumstances appear uncertain. It reminds us that truth can often be found beyond the surface, and by delving into the depths of our subconscious, we can uncover profound insights and revelations."
    },
    "The Sun": {
        "Number": 19,
        "Zodiac Sign": "Sun",
        "Planet": "Sun",
        "Hebrew Letter": "Resh (ר) - Head or Sun",
        "Position on Tree": "Path 30 (Hod to Yesod) - The Path of Resplendent Intelligence",
        "Assigned Colors": "Orange and Yellow - Embodiments of Joy and Enlightenment",
        "Summary": "The Sun card represents joy, vitality, and enlightenment. It symbolizes the radiance of the true self and the illumination of consciousness. Like the rising sun, this card brings a sense of optimism and warmth, encouraging us to embrace our inner light and express our authentic selves. The Sun invites us to celebrate life's simple pleasures and to bask in the abundance of positive energy around us. It signifies a period of clarity and growth, reminding us that by aligning with our highest purpose, we can shine brightly and inspire others in the process."
    },
    "The Aeon": {
        "Number": 20,
        "Zodiac Sign": "Pluto",
        "Planet": "Uranus",
        "Hebrew Letter": "Shin (ש) - Tooth or Fire",
        "Position on Tree": "Path 31 (Yesod to Malkuth) - The Path of Natural Intelligence",
        "Assigned Colors": "Purple and Gold - Symbolizing Transformation and Divinity",
        "Summary": "The Aeon card represents cosmic cycles, evolution, and the unfolding of destiny. It symbolizes the integration of past, present, and future. This card carries a profound message of transformation and alignment with the cosmic flow of existence. The Aeon invites us to embrace change as a natural part of life's unfolding, reminding us that by letting go of outdated beliefs and patterns, we can step into a higher state of consciousness. It signifies a period of profound change and self-discovery, encouraging us to awaken to our true potential and purpose."
    },
    "The Universe": {
        "Number": 21,
        "Zodiac Sign": "Saturn",
        "Planet": "Saturn",
        "Hebrew Letter": "Tau (ת) - Cross or Saturn",
        "Position on Tree": "Path 32 (Yesod to Malkuth) - The Path of Pure Intelligence",
        "Assigned Colors": "Black and Blue - Representing the Void and Cosmic Wisdom",
        "Summary": "The Universe card represents completion, wholeness, and the interconnectedness of all things. It symbolizes the culmination of a journey and the realization of a greater cosmic harmony. This card signifies the integration of diverse experiences and the achievement of a state of balance and unity. The Universe invites us to recognize the divine order within chaos and the interconnectedness of all life. It signifies a time of profound understanding and alignment with the universe's grand tapestry, reminding us that every ending is a new beginning and that we are an integral part of the cosmic dance."
    },
}


    "Prince of Swords": {
        "Number": 11,
        "Zodiac Sign": "Aquarius",
        "Element": "Air",
        "Hebrew Letter": "Kaf (כ) - Palm of the Hand or Aquarius",
        "Position on Tree": "Paths 12, 21, 30 (Chokmah to Tiphareth, Chesed, Netzach) - The Path of Intellectual Exploration and Expression",
        "Assigned Colors": "Light Blue and Silver - Signifying Clarity and Insight",
        "Summary": "The Prince of Swords embodies the energy of intellect, swift communication, and mental agility. As the fiery aspect of Air, this card symbolizes the application of mental prowess and logic to bring ideas into action. With the power of the Aquarian influence, the Prince of Swords is a visionary and innovative thinker, often ahead of their time. Their commitment to truth and objectivity drives them to analyze situations thoroughly, seeking clarity amidst complexity.\n\nThe Prince of Swords rides through life with a keen intellect and a quick-witted nature. Their approach is characterized by assertiveness and the pursuit of justice. However, this card also carries a warning about the potential for intellectual arrogance or impulsive action. The Prince's unyielding pursuit of truth can sometimes lead to the harsh delivery of words that cut deeper than intended.\n\nThe Prince of Swords stands at the crossroads of different realms, bridging Chokmah's inspired wisdom with Tiphareth's balanced expression. This card encourages us to harness the power of our minds, to seek new perspectives, and to use our intellectual abilities to bring about positive change. The Prince of Swords reminds us that while intellectual prowess is a valuable tool, it should be tempered with wisdom and empathy to avoid causing unintended harm."
    }
class TrianglePositions:
    def __init__(self):
        self.positions = {
            "level 0 far right": {
                "Number": 1,
                "Element": "Fire",
                "Attribute": "Will",
                "Alchemical Concepts": "Transformation, purification",
                "Esoteric Concepts": "Initiation, beginnings, the number 1 signifies the unity and the seed of creation. In Kabbalah, it corresponds to Kether, the highest Sephirah.",
                "Astrological Concepts": "Aries, Leo, Sagittarius",
                "Kabbalah Concepts": "Sephiroth of Kether, Chokmah, Binah",
                "Synopsis": "At the level 0 far right of the triangle, the position of Fire and Will represents the spark of creation and the driving force of action. Fire embodies the transformative power of change and the initiation of new cycles. Will embodies determination and the motivation to manifest one's desires. This position symbolizes the ignition of potential and the first steps on the spiritual journey. The number 1 signifies unity and the beginning of creation. In Kabbalah, this position corresponds to Kether, the highest Sephirah, representing the divine source of all creation."
            },
            "level 0 right": {
                "Number": 2,
                "Element": "Air",
                "Attribute": "Thought",
                "Alchemical Concepts": "Sublimation, volatilization",
                "Esoteric Concepts": "Intellect, communication, the number 2 signifies duality and balance. In Kabbalah, it corresponds to Chokmah and Binah, representing divine wisdom and understanding.",
                "Astrological Concepts": "Gemini, Libra, Aquarius",
                "Kabbalah Concepts": "Sephiroth of Chesed, Geburah, Tiphareth",
                "Synopsis": "At the level 0 right of the triangle, the position of Air and Thought represents the realm of intellect and communication. Air embodies the power of thought, ideas, and mental clarity. Thought symbolizes the process of contemplation and the exchange of ideas. This position signifies the foundation of logical understanding and the exploration of higher truths. The number 2 represents duality and balance, emphasizing the interplay of opposites. In Kabbalah, this position corresponds to Chokmah and Binah, the masculine and feminine aspects of divine wisdom and understanding."
            },
            "level 0 left": {
                "Number": 3,
                "Element": "Water",
                "Attribute": "Emotion",
                "Alchemical Concepts": "Dissolution, coagulation",
                "Esoteric Concepts": "Intuition, empathy, the number 3 signifies manifestation and creative expression. In Kabbalah, it corresponds to the Sephiroth of Netzach, Hod, Yesod.",
                "Astrological Concepts": "Cancer, Scorpio, Pisces",
                "Kabbalah Concepts": "Sephiroth of Netzach, Hod, Yesod",
                "Synopsis": "At the level 0 left of the triangle, the position of Water and Emotion represents the realm of feelings and intuition. Water embodies the depths of emotion and the currents of the subconscious. Emotion symbolizes the flow of inner experiences and the connection to intuition. This position signifies the exploration of inner landscapes and the ability to empathize with others. The number 3 represents manifestation and creativity, emphasizing the power of creative expression. In Kabbalah, this position corresponds to Netzach, Hod, and Yesod, representing the energies of victory, splendor, and foundation."
            },
            "level 0 far left": {
                "Number": 4,
                "Element": "Earth",
                "Attribute": "Body",
                "Alchemical Concepts": "Calcination, solidification",
                "Esoteric Concepts": "Manifestation, physical experience, the number 4 signifies stability and foundation. In Kabbalah, it corresponds to the Sephiroth of Malkuth, representing the material world.",
                "Astrological Concepts": "Taurus, Virgo, Capricorn",
                "Kabbalah Concepts": "Sephiroth of Malkuth",
                "Synopsis": "At the level 0 far left of the triangle, the position of Earth and Body represents the realm of physicality and manifestation. Earth embodies the material world and the tangible aspects of existence. Body symbolizes the vessel of the soul and the connection to the physical senses. This position signifies the grounding of spiritual energies into the physical realm and the experience of embodiment. The number 4 represents stability and foundation, highlighting the importance of a strong base. In Kabbalah, this position corresponds to Malkuth, the Sephirah that represents the material world and the point of entry for divine energies into manifestation."
            },
                "level 1 right": {
                "Number": 5,
                "Attribute": "Male",
                "Gender": "Masculine",
                "Alchemical Concepts": "Projection, activation",
                "Esoteric Concepts": "Yang, active principle, the number 5 signifies change and challenge. In Kabbalah, it is associated with Geburah.",
                "Astrological Concepts": "Mars",
                "Kabbalah Concepts": "Sephiroth of Geburah",
                "Synopsis": "At level 1 right of the triangle, the position of Male and Masculine represents the active and assertive qualities of existence. Male embodies the yang principle, representing dynamic energy and forward movement. Masculine qualities emphasize strength, initiation, and the pursuit of goals. This position symbolizes the assertive aspects of the self and the expression of personal power. The number 5 signifies change and challenge, highlighting the transformative nature of this position. In Kabbalah, this position corresponds to Geburah, representing severity and judgment."
            },
            "level 1 centre": {
                "Number": 6,
                "Attribute": "Herm (as the Greek concept of Hermes)",
                "Gender": "Androgynous",
                "Alchemical Concepts": "Union of opposites, synthesis",
                "Esoteric Concepts": "Balance, harmony, the number 6 signifies equilibrium and harmony. In Kabbalah, it is associated with Tiphareth, the Sephirah of beauty and balance.",
                "Astrological Concepts": "Mercury",
                "Kabbalah Concepts": "Sephiroth of Tiphareth",
                "Synopsis": "At level 1 centre of the triangle, the position of Herm and Androgynous represents the integration of opposites and the synthesis of diverse elements. Herm embodies the unity of masculine and feminine principles within the self. Androgynous qualities emphasize the balance between receptive and active energies. This position symbolizes the harmony achieved through unification and the recognition of inner completeness. The number 6 signifies equilibrium and harmony, highlighting the importance of finding balance in life. In Kabbalah, this position corresponds to Tiphareth, representing beauty, balance, and the blending of energies."
            },
            "level 1 left": {
                "Number": 7,
                "Attribute": "Female",
                "Gender": "Feminine",
                "Alchemical Concepts": "Fermentation, transformation",
                "Esoteric Concepts": "Intuition, nurturing, the number 7 signifies spiritual growth and development. In Kabbalah, it is associated with Netzach, the Sephirah of victory and emotion.",
                "Astrological Concepts": "Venus",
                "Kabbalah Concepts": "Sephiroth of Netzach",
                "Synopsis": "At level 1 left of the triangle, the position of Female and Feminine represents the receptive and nurturing qualities of existence. Female embodies the yin principle, representing receptivity, intuition, and nurturing. Feminine qualities emphasize compassion, sensitivity, and the connection to emotions. This position symbolizes the importance of intuitive insights and the ability to empathize with others. The number 7 signifies spiritual growth and development, highlighting the path of inner exploration and self-discovery. In Kabbalah, this position corresponds to Netzach, representing victory, emotions, and the cultivation of harmonious relationships."
            },
                "level 2 right": {
                "Number": 8,
                "Attribute": "Light",
                "Planet": "Sun",
                "Alchemical Concepts": "Illumination, enlightenment",
                "Esoteric Concepts": "Divine wisdom, enlightenment, the number 8 signifies cycles of growth and transformation. In Kabbalah, it is associated with Hod.",
                "Astrological Concepts": "Sun",
                "Kabbalah Concepts": "Sephiroth of Hod",
                "Synopsis": "At level 2 right of the triangle, the position of Light and Sun represents the illuminating power of divine wisdom and enlightenment. Light embodies the spiritual illumination that dispels darkness and reveals hidden truths. Sun qualities emphasize vitality, clarity, and enlightenment. This position symbolizes the radiance of the soul's journey and the pursuit of spiritual knowledge. The number 8 signifies cycles of growth and transformation, highlighting the ongoing evolution of the soul. In Kabbalah, this position corresponds to Hod, representing splendor and the sphere of intellect and communication."
            },
            "level 2 left": {
                "Number": 9,
                "Attribute": "Dark",
                "Planet": "Moon",
                "Alchemical Concepts": "Reflection, receptivity",
                "Esoteric Concepts": "Intuitive insights, the number 9 signifies completion and spiritual fulfillment. In Kabbalah, it is associated with Yesod.",
                "Astrological Concepts": "Moon",
                "Kabbalah Concepts": "Sephiroth of Yesod",
                "Synopsis": "At level 2 left of the triangle, the position of Dark and Moon represents the realm of intuitive insights and receptivity. Dark embodies the mysteries of the subconscious and the hidden realms of the soul. Moon qualities emphasize intuition, emotions, and the ebb and flow of life. This position symbolizes the reflective nature of the spiritual journey and the connection to the intuitive self. The number 9 signifies completion and spiritual fulfillment, highlighting the culmination of experiences. In Kabbalah, this position corresponds to Yesod, representing the foundation of the soul's journey and the realm of dreams and visions."
            },
            "level 3 Top": {
                "Number": 10,
                "Attribute": "Divine",
                "Planet": "Astral",
                "Alchemical Concepts": "Perfection, union",
                "Esoteric Concepts": "Transcendence, oneness, the number 10 signifies divine perfection and the completion of cycles. In Kabbalah, it is associated with Kether.",
                "Astrological Concepts": "Monad",
                "Kabbalah Concepts": "Sephiroth of Kether",
                "Synopsis": "At level 3 Top of the triangle, the position of Divine and Astral represents the transcendent nature of spiritual union and oneness. Divine embodies the ultimate source of all creation and the realm of the sacred. Astral qualities emphasize the connection to higher planes of existence and the journey beyond the material world. This position symbolizes the culmination of the soul's journey and the realization of unity with the divine. The number 10 signifies divine perfection and the completion of cycles, highlighting the integration of spiritual and material aspects. In Kabbalah, this position corresponds to Kether, representing the highest Sephirah and the divine source of all creation. This concept of unity and divine source is reminiscent of the Greek idea of Monad, a singular and divine principle from which all creation emanates."
            },
            },
        
triangle_positions = TrianglePositions()

thoth_major_arcana = ThothMajorArcana()

def read_triangle(self):
    def shuffle_deck():
        import random
        random.shuffle(self.deck)

    levels = [[4], [3], [2], [1]]
    triangle = []

    self.deck = list(self.cards.keys())
    shuffle_deck()

    for level in levels:
        row = []
        for _ in range(level[0]):
            if self.deck:
                card = self.deck.pop(0)
                row.insert(0, card)  # Place cards from right to left
        triangle.append(row)

    return triangle

# Creating an instance of the ThothMajorArcana class
thoth_major_arcana = ThothMajorArcana()

# Reading and printing the triangle layout
triangle_layout = thoth_major_arcana.read_triangle()
for row in triangle_layout:
    print(row)

magus_info = thoth_major_arcana.cards["The Magus"]
print("Number:", magus_info["Number"])
print("Zodiac Sign:", magus_info["Zodiac Sign"])
print("Planet:", magus_info["Planet"])
print("Summary:", magus_info["Summary"])
