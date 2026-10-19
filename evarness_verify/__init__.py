"""evarness — prove an AI agent harness before it touches real data.

``import evarness_verify`` gives you the batteries-included surface: the kernel plus
the agents domain, with plugins discovered — loaded lazily, on first
attribute access. For the bare kernel (e.g. when building your own domain),
import from ``evarness_verify.core`` directly — it never loads a domain behind your
back, and ``tests/test_architecture_boundaries.py`` holds that promise.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  # static types for the lazy surface
    from evarness_verify.core.errors import (
        EvarnessError as EvarnessError,
    )
    from evarness_verify.core.errors import (
        GraphValidationError as GraphValidationError,
    )
    from evarness_verify.core.errors import (
        NodeBlocked as NodeBlocked,
    )
    from evarness_verify.core.errors import (
        RegistryError as RegistryError,
    )
    from evarness_verify.core.errors import (
        RunPaused as RunPaused,
    )
    from evarness_verify.core.executor import (
        Emitter as Emitter,
    )
    from evarness_verify.core.executor import (
        RunContext as RunContext,
    )
    from evarness_verify.core.executor import (
        RunResult as RunResult,
    )
    from evarness_verify.core.executor import (
        execute as execute,
    )
    from evarness_verify.core.graph import (
        GraphModel as GraphModel,
    )
    from evarness_verify.core.graph import (
        lint as lint,
    )
    from evarness_verify.core.graph import (
        migrate as migrate,
    )
    from evarness_verify.core.graph import (
        topological_order as topological_order,
    )
    from evarness_verify.core.invariants import (
        check_invariants as check_invariants,
    )
    from evarness_verify.core.invariants import (
        load_invariant_defs as load_invariant_defs,
    )
    from evarness_verify.core.prove import prove as prove
    from evarness_verify.core.prove import verify_proof as verify_proof
    from evarness_verify.core.registry import (
        NODE_TYPES as NODE_TYPES,
    )
    from evarness_verify.core.registry import (
        load_entry_point_plugins as load_entry_point_plugins,
    )
    from evarness_verify.core.trace import canonical_trace as canonical_trace
    from evarness_verify.core.trace import trace_digest as trace_digest
    from evarness_verify.domains import agents as agents
    from evarness_verify.domains.agents.sim import Fixture as Fixture
    from evarness_verify.domains.agents.sim import load_fixture as load_fixture

__version__ = "0.1.0a1"

__all__ = [
    "NODE_TYPES",
    "Emitter",
    "EvarnessError",
    "Fixture",
    "GraphModel",
    "GraphValidationError",
    "NodeBlocked",
    "RegistryError",
    "RunContext",
    "RunPaused",
    "RunResult",
    "__version__",
    "agents",
    "canonical_trace",
    "check_invariants",
    "execute",
    "lint",
    "load_entry_point_plugins",
    "load_fixture",
    "load_invariant_defs",
    "migrate",
    "prove",
    "topological_order",
    "trace_digest",
    "verify_proof",
]

_surface: dict[str, Any] = {}


def _load_surface() -> dict[str, Any]:
    from evarness_verify.core import errors, executor, graph, invariants, prove, registry, trace
    from evarness_verify.domains import agents
    from evarness_verify.domains.agents import sim

    registry.load_entry_point_plugins()
    return {
        "EvarnessError": errors.EvarnessError,
        "GraphValidationError": errors.GraphValidationError,
        "NodeBlocked": errors.NodeBlocked,
        "RegistryError": errors.RegistryError,
        "RunPaused": errors.RunPaused,
        "Emitter": executor.Emitter,
        "RunContext": executor.RunContext,
        "RunResult": executor.RunResult,
        "execute": executor.execute,
        "GraphModel": graph.GraphModel,
        "lint": graph.lint,
        "migrate": graph.migrate,
        "topological_order": graph.topological_order,
        "check_invariants": invariants.check_invariants,
        "load_invariant_defs": invariants.load_invariant_defs,
        "prove": prove.prove,
        "verify_proof": prove.verify_proof,
        "NODE_TYPES": registry.NODE_TYPES,
        "load_entry_point_plugins": registry.load_entry_point_plugins,
        "canonical_trace": trace.canonical_trace,
        "trace_digest": trace.trace_digest,
        "Fixture": sim.Fixture,
        "load_fixture": sim.load_fixture,
        "agents": agents,
    }


def __getattr__(name: str) -> Any:
    if name in __all__:
        if not _surface:
            _surface.update(_load_surface())
        return _surface[name]
    raise AttributeError(f"module 'evarness' has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))
