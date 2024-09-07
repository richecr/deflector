from sentinel import affirm, describe, it


def main() -> int:
    return 2


@describe("Main 1")
def describe_main() -> None:
    @it("It Test 1")
    def test1() -> None:
        v = main()
        affirm.equal(v, 2, "Equal 1")
        affirm.equal(v, 2, "Equal 2")

    @it("It Test 2")
    def test2() -> None:
        v = main()
        affirm.equal(v, 2, "Equal")
        affirm.not_equal(v, 1, "Not Equal")
        affirm.ok(True, "Ok")
        affirm.match_re("acab", "ab", "Match Re")
        affirm.does_not_match_re("a", "ab", "Does Not Match Re")


@describe("Main 2")
def describe_main_2() -> None:
    @it("It Test 1")
    def test1() -> None:
        v = main()
        affirm.equal(v, 2, "Equal 1")
        affirm.equal(v, 2, "Equal 2")

    @it("It Test 2")
    def test2() -> None:
        v = main()
        affirm.equal(v, 2, "Equal")
        affirm.not_equal(v, 1, "Not Equal")
        affirm.ok(True, "Ok")
        affirm.match_re("acab", "ab", "Match Re")
        affirm.does_not_match_re("a", "ab", "Does Not Match Re")


affirm.equal(1, 1, "Ops")
