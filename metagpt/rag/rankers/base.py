"""Base Ranker."""

from abc import abstractmethod
from typing import Optional

from llama_index import QueryBundle
from llama_index.postprocessor.types import BaseNodePostprocessor
from llama_index.schema import NodeWithScore


class RAGRanker(BaseNodePostprocessor):
    """inherit from llama_index"""

    @abstractmethod
    def _postprocess_nodes(
        self,
        nodes: list[NodeWithScore],
        query_bundle: Optional[QueryBundle] = None,
    ) -> list[NodeWithScore]:
        """postprocess nodes."""
