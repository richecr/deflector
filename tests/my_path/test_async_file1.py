import asyncio

from sentinel import affirm
from sentinel.helpers.after_each import after_each
from sentinel.helpers.before_each import before_each
from sentinel.helpers.describe import describe
from sentinel.helpers.it import it


async def main() -> int:
    await asyncio.sleep(1)
    return 2


@describe("Main 1")
def describe_main() -> None:
    x = 1

    @before_each()
    async def start() -> bool:
        nonlocal x
        await asyncio.sleep(1)
        x += 1
        return True

    @after_each()
    async def end_() -> bool:
        nonlocal x
        await asyncio.sleep(1)
        x = 1
        return True

    @it("It Test 1")
    async def test1() -> None:
        v = await main()
        affirm.equal(x, 2, "Equal Before Each")
        affirm.equal(v, 2, "Equal 1")
        affirm.equal(v, 2, "Equal 2")

    @it.skip("It Test 2")
    async def test2() -> None:
        v = await main()
        affirm.equal(x, 2, "Equal After Each")
        affirm.equal(v, 2, "Equal")
        affirm.not_equal(v, 1, "Not Equal")
        affirm.ok(True, "Ok")
        affirm.match_re("acab", "ab", "Match Re")
        affirm.does_not_match_re("a", "ab", "Does Not Match Re")


affirm.equal(1, 1, "Ops")
