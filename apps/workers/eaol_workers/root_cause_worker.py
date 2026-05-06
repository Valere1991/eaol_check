"""Camunda worker placeholder for local alpha.

Production target: Zeebe job workers for BPMN service tasks:
- collect_context
- run_causal_reasoning
- create_recommendations
- wait_for_human_approval
- execute_approved_action
"""

import asyncio


async def main() -> None:
    print("EAOL Camunda worker placeholder. Wire pyzeebe here when Zeebe is running.")


if __name__ == "__main__":
    asyncio.run(main())
