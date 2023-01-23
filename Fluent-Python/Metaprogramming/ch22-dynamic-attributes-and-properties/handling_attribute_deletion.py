class BlackKnight:
    def __init__(self) -> None:
        self.phrases = [
            ("an arm", "'tis but a scratch."),
            ("another arm", "It's just a flesh wound"),
            ("a leg", "I'm invincible!"),
            ("another leg", "all right, we'll call it a draw."),
        ]

    @property
    def member(self):
        print("next member is:")
        return self.phrases[0][0]

    @member.deleter
    def member(self):
        member, text = self.phrases.pop(0)
        print(f"BLACK KNIGHT (loses {member}) -- {text}")


knight = BlackKnight()

del knight.member
del knight.member
del knight.member
del knight.member
