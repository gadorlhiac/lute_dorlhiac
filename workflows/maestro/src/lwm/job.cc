#include "lwm/job.hh"

#include <stdexcept>
#include <string>

namespace LWM {
  std::string rule_to_string(TriggerRule& rule) {
    switch (rule) {
    case TriggerRule::ALL_SUCCESS:
      return "ALL_SUCCESS";
    case TriggerRule::ANY_SUCCESS:
      return "ANY_SUCCESS";
    case TriggerRule::ALL_COMPLETED:
      return "ALL_COMPLETED";
    case TriggerRule::ALL_FAILED:
      return "ALL_FAILED";
    case TriggerRule::ANY_FAILED:
      return "ANY_FAILED";
    case TriggerRule::ALWAYS:
      return "ALWAYS";
    default:
      throw std::runtime_error("Unrecognized TriggerRule.");
    }
  }

  bool JobIdentifier::same_dag(const JobIdentifier& id_a, const JobIdentifier& id_b) {
    if (!id_a.job_key.empty() && !id_b.job_key.empty()) {
      const std::string prefix_key {
        id_a.job_key.size() > id_b.job_key.size() ? id_b.job_key : id_a.job_key
      };
      const std::string job_key {
        id_a.job_key.size() > id_b.job_key.size() ? id_a.job_key : id_b.job_key
      };

      const std::size_t pos { prefix_key.size() };
      if (job_key.compare(0, pos, prefix_key) == 0) {
        return true;
      }
    }

    return false;
  }

  bool JobIdentifier::matches(const JobIdentifier& partial, const JobIdentifier& full) {
    if (!partial.job_key.empty() && partial.job_key != full.job_key) {
      return false;
    }

    if (partial.name && full.name != partial.name) {
      return false;
    }

    if (!partial.launch_id.empty() && partial.launch_id != full.launch_id) {
      return false;
    }

    return true;
  }

  bool JobIdentifier::compatible(const JobIdentifier& id_a, const JobIdentifier& id_b) {
    if (!id_a.job_key.empty() && !id_b.job_key.empty() && id_a.job_key != id_b.job_key) {
      return false;
    }

    if (id_a.name && id_b.name && *(id_a.name) != *(id_b.name)) {
      return false;
    }

    if (!id_a.launch_id.empty() &&
        !id_b.launch_id.empty() &&
        id_a.launch_id != id_b.launch_id) {
      return false;
    }

    return true;
  }
} // namespace LWM
