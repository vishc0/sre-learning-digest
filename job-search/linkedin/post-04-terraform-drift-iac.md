# Post 4: Terraform Import — IaC/Drift Story

---

A 4am phone call, a production deployment on hold, and a Terraform state file that did not match reality. Here is the story.

We had inherited infrastructure. Built by hand, years earlier, by engineers who were no longer at the company. No IaC. No state file. Just AWS resources running in production and a deployment pipeline that expected Terraform to manage them.

The new deployment would have created duplicate resources — or worse, destroyed the existing ones — because Terraform saw them as unknown.

The answer was `terraform import`. If you have not used it: it is the command that says "this resource already exists in the real world — adopt it into your state file without recreating it." One resource at a time. With the correct resource address and the cloud resource ID.

We spent three hours that night mapping 40+ AWS resources to their Terraform equivalents, running imports, validating that `terraform plan` showed no diff before we touched anything. The deployment went out at 7am. No customer impact.

The leadership lesson: infrastructure drift is not a technical problem. It is a governance problem. Drift happens when teams are under pressure and the fastest path is a console click, not a pull request. The solution is not stricter rules — it is making the IaC path faster and safer than the manual path.

`terraform import` is a rescue tool. The goal is to never need rescue.

How does your team handle the gap between what Terraform thinks exists and what actually runs in production?

#Terraform #IaC #DevSecOps #SRE #PlatformEngineering #CloudEngineering #InfrastructureAsCode
