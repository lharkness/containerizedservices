package services.containerized.emailservice;

import io.dropwizard.Configuration;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.hibernate.validator.constraints.NotEmpty;

public class EmailServiceConfiguration extends Configuration {
	
	@NotEmpty
	private String secretApiKey;

	@NotEmpty
	private String publicApiKey;

	@NotEmpty
	private String resourceBase;

	@JsonProperty
	public String getSecretApiKey() {
		return this.secretApiKey;
	}

	@JsonProperty
	public String getPublicApiKey() {
		return this.publicApiKey;
	}

	@JsonProperty
	public String getResourceBase() {
		return this.resourceBase;
	}

	@JsonProperty
	public void setSecretApiKey(String secretKey) {
		this.secretApiKey = secretKey;
	}

	@JsonProperty	
	public void setPublicApiKey(String publicKey) {
		this.publicApiKey = publicKey;
	}

	@JsonProperty
	public void setResourceBase(String resourceBase) {
		this.resourceBase = resourceBase;
	}

}
