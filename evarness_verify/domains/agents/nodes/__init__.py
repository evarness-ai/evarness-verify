"""Node registry — the agents domain's node set, grouped by concern.

Importing this package registers every node type into the kernel's
``NODE_TYPES`` registry. Add a node by writing a ``NodeSpec`` subclass with
``@register`` in the fitting module (or your own plugin) — the palette, lint,
and executor pick it up from the registry.
"""

from evarness_verify.core.errors import NodeBlocked, RunPaused  # noqa: F401  (compat re-export)
from evarness_verify.domains.agents.nodes.base import (  # noqa: F401
    DEFAULT_AGENT_SYSTEM,
    DEFAULT_LLM_SYSTEM,
    NODE_PRESENTATION,
    REGISTRY,
    NodeSpec,
    as_text,
    presentation,
)
from evarness_verify.domains.agents.nodes.basic import (  # noqa: F401
    InputNode,
    LLMNode,
    OutputNode,
    OutputParserNode,
    PromptTemplateNode,
)
from evarness_verify.domains.agents.nodes.governance import (  # noqa: F401
    ApprovalGateNode,
    DataClassifierNode,
    IntentRouterNode,
    InterceptorNode,
    JudgeChainNode,
    LLMGuardNode,
    LLMJudgeNode,
    PolicyGateNode,
    RateBudgetLimiterNode,
    RedactionRulesNode,
    TierRouterNode,
)
from evarness_verify.domains.agents.nodes.loop import LoopControllerNode  # noqa: F401
from evarness_verify.domains.agents.nodes.memory import (  # noqa: F401
    ConversationBufferNode,
    EpisodicMemoryNode,
    ProceduralMemoryNode,
    SemanticMemoryNode,
    SummaryConsolidatorNode,
    WorkingMemoryNode,
)
from evarness_verify.domains.agents.nodes.observability import (  # noqa: F401
    AuditLogSinkNode,
    CostLatencyMonitorNode,
    MetricsEmitterNode,
    TraceProbeNode,
)
from evarness_verify.domains.agents.nodes.rag import (
    ContextAssemblerNode,  # noqa: F401
    RetrieverNode,  # noqa: F401
)
from evarness_verify.domains.agents.nodes.tools import ToolNode  # noqa: F401
from evarness_verify.domains.agents.prompts import (  # noqa: F401  (compat re-export)
    DEFAULTS,
    NUDGES,
    PROMPT_TEMPLATES,
    PROTOCOLS,
)
