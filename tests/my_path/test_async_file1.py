import asyncio

from sentinel.helpers.describe import describe
from sentinel.helpers.it import it
from sentinel.modules.essentials.ensure import ensure


async def main() -> int:
    await asyncio.sleep(1)
    return 2


@describe("Main 1")
def describe_main() -> None:
    @it("It Test 1")
    async def test1() -> None:
        v = await main()
        ensure.equal(v, 2, "Equal 1")
        ensure.equal(v, 2, "Equal 2")

    @it("It Test 2")
    async def test2() -> None:
        v = await main()
        ensure.equal(v, 2, "Equal")
        ensure.not_equal(v, 1, "Not Equal")
        ensure.ok(True, "Ok")
        ensure.match_re("acab", "ab", "Match Re")
        ensure.does_not_match_re("a", "ab", "Does Not Match Re")


ensure.equal(1, 1, "Ops")
