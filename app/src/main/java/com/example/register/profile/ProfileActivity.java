package com.example.register.profile;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.example.register.R;

public class ProfileActivity extends AppCompatActivity {

    private Button btnviewprf, btnsalelist;
    private ImageView imageView;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        btnviewprf = findViewById(R.id.btnviewprf);
        btnsalelist = findViewById(R.id.btnsalelist);
        imageView = findViewById(R.id.imageView);

        btnviewprf.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ProfileActivity.this, com.example.register.profile.UserActivity.class);
                startActivity(intent);
            }
        });

        btnsalelist.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Intent 정보를 넘겨줌
                Intent intent = getIntent();
                String username = intent.getStringExtra("username");

                Intent salelistIntent = new Intent(ProfileActivity.this, com.example.register.profile.SalelistActivity.class);
                salelistIntent.putExtra("username", username);
                startActivity(salelistIntent);
            }
        });
    }
}