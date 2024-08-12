from sentinel.helpers.describe import describe
from sentinel.helpers.it import it
from sentinel.modules.essentials.ensure import ensure


def main() -> int:
    return 2


def test1() -> None:
    v = main()
    ensure.equal(v, 2, "Equal 1")
    ensure.equal(v, 2, "Equal 2")


def test2() -> None:
    v = main()
    ensure.equal(v, 2, "Equal")
    ensure.not_equal(v, 1, "Not Equal")
    ensure.ok(True, "Ok")
    ensure.match_re("acab", "ab", "Match Re")
    ensure.does_not_match_re("a", "a", "Does Not Match Re")


def describe_main() -> None:
    it("It Test 1", lambda: test1())
    it("It Test 2", lambda: test2())


describe("Main 1", lambda: describe_main())

describe("Main 2", lambda: describe_main())

ensure.equal(1, 1, "Ops")
